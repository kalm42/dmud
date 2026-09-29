import asyncio
import logging
import sqlite3
from contextlib import suppress
from pathlib import Path

import pytest

from dmud.operations.accept_operation import accept_operation
from dmud.operations.execution_hooks import ExecutionHooks
from dmud.operations.get_events import get_events
from dmud.operations.get_operation import get_operation
from dmud.operations.models import Operation, RecoveryCommand
from dmud.operations.recover_operation import recover_operation
from dmud.operations.run_worker import run_worker
from dmud.platform.sqlite.initialize_database import initialize_database
from dmud.session_zero.models import CreateSessionZeroDraft


async def wait_for_status(path: Path, operation_id: str, status: str) -> Operation:
    async with asyncio.timeout(3):
        while True:
            operation = await asyncio.to_thread(get_operation, path, operation_id)
            if operation.status == status:
                return operation
            await asyncio.sleep(0.01)


def test_worker_processes_healthy_work_beside_a_corrupt_record(tmp_path: Path) -> None:
    path = initialize_database(tmp_path)
    damaged = accept_operation(
        path,
        CreateSessionZeroDraft(requestId="req_00000000-0000-4000-8000-000000000041"),
    )
    with sqlite3.connect(path) as db:
        db.execute(
            "UPDATE operations SET resource = json_remove(resource, '$.requestId') WHERE operation_id = ?",
            (damaged.operation_id,),
        )
    healthy = accept_operation(
        path,
        CreateSessionZeroDraft(requestId="req_00000000-0000-4000-8000-000000000042"),
    )

    async def scenario() -> Operation:
        wake = asyncio.Event()
        worker = asyncio.create_task(run_worker(path, wake, ExecutionHooks()))
        wake.set()
        try:
            return await wait_for_status(path, healthy.operation_id, "complete")
        finally:
            worker.cancel()
            with suppress(asyncio.CancelledError):
                await worker

    assert asyncio.run(scenario()).commit_boundary == "draft"


def test_worker_finishes_committed_delivery_after_an_io_failure(tmp_path: Path) -> None:
    path = initialize_database(tmp_path)
    original = accept_operation(
        path,
        CreateSessionZeroDraft(requestId="req_00000000-0000-4000-8000-000000000043"),
    )

    async def fail_delivery(operation_id: str) -> None:
        raise OSError("Controlled delivery failure")

    async def scenario() -> Operation:
        wake = asyncio.Event()
        worker = asyncio.create_task(
            run_worker(path, wake, ExecutionHooks(after_commit=fail_delivery))
        )
        wake.set()
        try:
            return await wait_for_status(path, original.operation_id, "complete")
        finally:
            worker.cancel()
            with suppress(asyncio.CancelledError):
                await worker

    assert asyncio.run(scenario()).committed_revision == 1
    with sqlite3.connect(path) as db:
        assert db.execute("SELECT count(*) FROM draft_commits").fetchone()[0] == 1


def test_worker_recovers_when_failure_recording_is_temporarily_unavailable(
    tmp_path: Path, caplog: pytest.LogCaptureFixture
) -> None:
    path = initialize_database(tmp_path)
    original = accept_operation(
        path,
        CreateSessionZeroDraft(requestId="req_00000000-0000-4000-8000-000000000044"),
    )
    with sqlite3.connect(path) as db:
        db.execute(
            "CREATE TRIGGER block_commit BEFORE INSERT ON request_results BEGIN SELECT RAISE(ABORT, 'controlled failure'); END"
        )
        db.execute(
            "CREATE TRIGGER block_failure BEFORE UPDATE ON operations WHEN json_extract(NEW.resource, '$.status') = 'failed' BEGIN SELECT RAISE(ABORT, 'controlled failure'); END"
        )
    caplog.set_level(logging.WARNING)

    async def scenario() -> Operation:
        wake = asyncio.Event()
        worker = asyncio.create_task(run_worker(path, wake, ExecutionHooks()))
        wake.set()
        try:
            async with asyncio.timeout(3):
                while not caplog.records:
                    await asyncio.sleep(0.01)
            with sqlite3.connect(path) as db:
                db.execute("DROP TRIGGER block_failure")
            return await wait_for_status(path, original.operation_id, "failed")
        finally:
            worker.cancel()
            with suppress(asyncio.CancelledError):
                await worker

    assert asyncio.run(scenario()).commit_boundary == "none"


def test_old_attempt_failure_cannot_fail_an_accepted_retry(tmp_path: Path) -> None:
    path = initialize_database(tmp_path)
    original = accept_operation(
        path,
        CreateSessionZeroDraft(requestId="req_00000000-0000-4000-8000-000000000050"),
    )

    async def scenario() -> Operation:
        reached = asyncio.Event()
        release = asyncio.Event()

        async def fail_old_attempt(operation_id: str) -> None:
            if not reached.is_set():
                reached.set()
                await release.wait()
                raise OSError("Controlled stale attempt failure")

        wake = asyncio.Event()
        worker = asyncio.create_task(
            run_worker(path, wake, ExecutionHooks(before_commit=fail_old_attempt))
        )
        wake.set()
        try:
            async with asyncio.timeout(3):
                await reached.wait()
            running = get_operation(path, original.operation_id)
            cancelled = recover_operation(
                path,
                original.operation_id,
                RecoveryCommand(
                    requestId="req_00000000-0000-4000-8000-000000000051",
                    expectedLastEventId=running.last_event_id,
                ),
                "cancel",
            )
            recover_operation(
                path,
                original.operation_id,
                RecoveryCommand(
                    requestId="req_00000000-0000-4000-8000-000000000052",
                    expectedLastEventId=cancelled.last_event_id,
                ),
                "retry",
            )
            release.set()
            return await wait_for_status(path, original.operation_id, "complete")
        finally:
            worker.cancel()
            with suppress(asyncio.CancelledError):
                await worker

    assert asyncio.run(scenario()).commit_boundary == "draft"
    assert "failed" not in [
        event.operation.status for event in get_events(path, original.operation_id, 0)
    ]
