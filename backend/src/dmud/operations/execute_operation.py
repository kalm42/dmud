import asyncio
from pathlib import Path

from dmud.operations.claim_operation import claim_operation
from dmud.operations.commit_draft import commit_draft
from dmud.operations.execution_failure import ExecutionFailure
from dmud.operations.execution_hooks import ExecutionHooks
from dmud.operations.models import Operation
from dmud.operations.transition_operation import transition_operation
from dmud.platform.sqlite.run_database import run_database


async def execute_operation(
    path: Path, operation: Operation, hooks: ExecutionHooks
) -> None:
    """Execute one claimed attempt independently of delivery consumers; e.g. await execute_operation(path, operation, hooks)."""
    attempt_event_id = operation.last_event_id
    try:
        current = operation
        if operation.result is None:
            claimed = await run_database(claim_operation, path, operation.operation_id)
            if claimed is None:
                return
            current = claimed
            attempt_event_id = current.last_event_id
            if hooks.before_commit is not None:
                await hooks.before_commit(operation.operation_id)
            current = await run_database(
                commit_draft, path, operation.operation_id, attempt_event_id
            )
            if current.result is not None and hooks.after_commit is not None:
                await hooks.after_commit(operation.operation_id)
        if current.result is not None:
            await run_database(
                transition_operation, path, operation.operation_id, "complete"
            )
    except asyncio.CancelledError:
        raise
    except Exception:  # noqa: BLE001 — execution boundary retains only the failed attempt identity
        raise ExecutionFailure(operation.operation_id, attempt_event_id) from None
