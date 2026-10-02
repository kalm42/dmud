import asyncio
import logging
from pathlib import Path

from dmud.operations.execute_operation import execute_operation
from dmud.operations.execution_failure import ExecutionFailure
from dmud.operations.execution_hooks import ExecutionHooks
from dmud.operations.list_nonterminal import list_nonterminal
from dmud.operations.settle_execution_failure import settle_execution_failure
from dmud.platform.sqlite.run_database import run_database


async def run_worker(path: Path, wake: asyncio.Event, hooks: ExecutionHooks) -> None:
    """Supervise durable commands independently of consumers; e.g. create_task(run_worker(path, wake, hooks))."""
    failures: dict[str, ExecutionFailure] = {}
    logger = logging.getLogger(__name__)
    while True:
        await wake.wait()
        wake.clear()
        retry_scan = False
        for operation_id, failure in list(failures.items()):
            try:
                await run_database(settle_execution_failure, path, failure)
                del failures[operation_id]
            except Exception:  # noqa: BLE001 — supervision keeps unavailable failure persistence retryable
                logger.warning("Operation failure recovery unavailable; retrying.")
        try:
            operations = await run_database(list_nonterminal, path)
        except Exception:  # noqa: BLE001 — a storage scan failure must not stop supervision
            logger.warning("Operation work scan unavailable; retrying.")
            operations = []
            retry_scan = True
        for operation in operations:
            if operation.operation_id in failures:
                continue
            try:
                await execute_operation(path, operation, hooks)
            except ExecutionFailure as failure:
                failures[operation.operation_id] = failure
        if failures or retry_scan:
            await asyncio.sleep(0.2)
            wake.set()
