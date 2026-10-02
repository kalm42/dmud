import asyncio
import sqlite3
import threading
from pathlib import Path

from fastapi.testclient import TestClient

from dmud.main import create_app
from dmud.operations.execution_hooks import ExecutionHooks
from dmud.platform.settings import Settings

REQUEST = {"requestId": "req_00000000-0000-4000-8000-000000000010"}


def test_precommit_cancel_prevents_draft(tmp_path: Path) -> None:
    gate = asyncio.Event()
    reached = threading.Event()

    async def pause(operation_id: str) -> None:
        reached.set()
        await gate.wait()

    with TestClient(
        create_app(
            settings=Settings(application_data_directory=tmp_path),
            execution_hooks=ExecutionHooks(before_commit=pause),
        )
    ) as client:
        operation = client.post("/api/session-zero-drafts", json=REQUEST).json()
        assert reached.wait(5)
        status = client.get(operation["statusUrl"]).json()
        assert status["status"] == "validating"
        draft = client.get("/api/session-zero-drafts/" + status["subject"]["draftId"])
        assert draft.status_code == 404
        assert draft.json()["code"] == "draft_not_committed"
        cancelled = client.post(
            operation["statusUrl"] + "/cancel",
            json={
                "requestId": "req_00000000-0000-4000-8000-000000000011",
                "expectedLastEventId": status["lastEventId"],
            },
        ).json()
        assert cancelled["status"] == "interrupted"
        assert cancelled["commitBoundary"] == "none"
        client.portal.call(gate.set)
    with sqlite3.connect(tmp_path / "dmud.sqlite3") as db:
        assert db.execute("SELECT count(*) FROM session_zero_drafts").fetchone()[0] == 0


def test_after_commit_cancel_preserves_original_result(tmp_path: Path) -> None:
    gate = asyncio.Event()
    reached = threading.Event()

    async def pause(operation_id: str) -> None:
        reached.set()
        await gate.wait()

    settings = Settings(application_data_directory=tmp_path)
    with TestClient(
        create_app(
            settings=settings, execution_hooks=ExecutionHooks(after_commit=pause)
        )
    ) as client:
        operation = client.post("/api/session-zero-drafts", json=REQUEST).json()
        assert reached.wait(5)
        status = client.get(operation["statusUrl"]).json()
        assert status["status"] == "committed"
        cancelled = client.post(
            operation["statusUrl"] + "/cancel",
            json={
                "requestId": "req_00000000-0000-4000-8000-000000000011",
                "expectedLastEventId": 1,
            },
        ).json()
        assert cancelled["result"] == status["result"]
        assert (
            client.get(
                "/api/session-zero-drafts/" + status["subject"]["draftId"]
            ).json()["draftRevision"]
            == 1
        )
    with TestClient(create_app(settings=settings)) as client:
        recovered = client.get(operation["statusUrl"]).json()
        assert recovered["status"] == "complete"
        assert recovered["result"] == status["result"]
    with sqlite3.connect(tmp_path / "dmud.sqlite3") as db:
        assert db.execute("SELECT count(*) FROM draft_commits").fetchone()[0] == 1


def test_worker_write_failure_is_recoverable_without_partial_draft(
    tmp_path: Path,
) -> None:
    gate = asyncio.Event()
    reached = threading.Event()

    async def pause(operation_id: str) -> None:
        reached.set()
        await gate.wait()

    with TestClient(
        create_app(
            settings=Settings(application_data_directory=tmp_path),
            execution_hooks=ExecutionHooks(before_commit=pause),
        )
    ) as client:
        operation = client.post("/api/session-zero-drafts", json=REQUEST).json()
        assert reached.wait(5)
        with sqlite3.connect(tmp_path / "dmud.sqlite3") as db:
            db.execute(
                "CREATE TRIGGER inject_failure BEFORE INSERT ON request_results BEGIN SELECT RAISE(ABORT, 'controlled write failure'); END"
            )
        client.portal.call(gate.set)
        with client.stream("GET", operation["eventsUrl"]) as stream:
            assert '"status":"failed"' in stream.read().decode()
        status = client.get(operation["statusUrl"]).json()
        assert status["recovery"]["retry"] is True
        with sqlite3.connect(tmp_path / "dmud.sqlite3") as db:
            db.execute("DROP TRIGGER inject_failure")
        retry = {
            "requestId": "req_00000000-0000-4000-8000-000000000011",
            "expectedLastEventId": status["lastEventId"],
        }
        response = client.post(operation["statusUrl"] + "/retry", json=retry)
        assert response.status_code == 202
        with client.stream("GET", operation["eventsUrl"]) as stream:
            assert '"status":"complete"' in stream.read().decode()
        assert (
            client.post(operation["statusUrl"] + "/retry", json=retry).json()[
                "operationId"
            ]
            == response.json()["operationId"]
        )
        assert client.get(operation["statusUrl"]).json()["subject"] == status["subject"]


def test_corrupt_read_is_a_typed_unavailable_problem(tmp_path: Path) -> None:
    with TestClient(
        create_app(settings=Settings(application_data_directory=tmp_path))
    ) as client:
        operation = client.post("/api/session-zero-drafts", json=REQUEST).json()
        with client.stream("GET", operation["eventsUrl"]) as stream:
            stream.read()
        valid = client.get(operation["statusUrl"]).text
        with sqlite3.connect(tmp_path / "dmud.sqlite3") as db:
            db.execute(
                "UPDATE operations SET resource = '{}' WHERE operation_id = ?",
                (operation["operationId"],),
            )
        response = client.get(operation["statusUrl"])
        assert response.status_code == 503
        assert response.json()["code"] == "operation_unavailable"
        with sqlite3.connect(tmp_path / "dmud.sqlite3") as db:
            db.execute(
                "UPDATE operations SET resource = ? WHERE operation_id = ?",
                (valid, operation["operationId"]),
            )


def test_restart_before_commit_requires_explicit_same_subject_retry(
    tmp_path: Path,
) -> None:
    gate = asyncio.Event()
    reached = threading.Event()

    async def pause(operation_id: str) -> None:
        reached.set()
        await gate.wait()

    settings = Settings(application_data_directory=tmp_path)
    with TestClient(
        create_app(
            settings=settings, execution_hooks=ExecutionHooks(before_commit=pause)
        )
    ) as client:
        operation = client.post("/api/session-zero-drafts", json=REQUEST).json()
        assert reached.wait(5)
    with TestClient(create_app(settings=settings)) as client:
        interrupted = client.get(operation["statusUrl"]).json()
        assert interrupted["status"] == "interrupted"
        assert interrupted["subject"] == operation["subject"]
        response = client.post(
            operation["statusUrl"] + "/retry",
            json={
                "requestId": "req_00000000-0000-4000-8000-000000000011",
                "expectedLastEventId": interrupted["lastEventId"],
            },
        )
        assert response.json()["operationId"] == operation["operationId"]
        with client.stream("GET", operation["eventsUrl"]) as stream:
            stream.read()
        assert client.get(operation["statusUrl"]).json()["status"] == "complete"


def test_stale_recovery_cannot_launch_a_new_attempt(tmp_path: Path) -> None:
    gate = asyncio.Event()
    reached = threading.Event()

    async def pause(operation_id: str) -> None:
        reached.set()
        await gate.wait()

    with TestClient(
        create_app(
            settings=Settings(application_data_directory=tmp_path),
            execution_hooks=ExecutionHooks(before_commit=pause),
        )
    ) as client:
        operation = client.post("/api/session-zero-drafts", json=REQUEST).json()
        assert reached.wait(5)
        response = client.post(
            operation["statusUrl"] + "/cancel",
            json={
                "requestId": "req_00000000-0000-4000-8000-000000000011",
                "expectedLastEventId": 1,
            },
        )
        assert response.status_code == 409
        assert response.json()["code"] == "stale_event"
        assert response.json()["operation"]["status"] == "validating"
