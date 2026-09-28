import asyncio
from pathlib import Path

from dmud.operations.claim_operation import claim_operation
from dmud.operations.commit_draft import commit_draft
from dmud.operations.execution_hooks import ExecutionHooks
from dmud.operations.list_nonterminal import list_nonterminal
from dmud.operations.transition_operation import transition_operation


async def run_worker(path: Path, wake: asyncio.Event, hooks: ExecutionHooks) -> None:
    """Supervise durable commands independently of consumers; e.g. create_task(run_worker(path, wake, hooks))."""
    while True:
        await wake.wait()
        wake.clear()
        for operation in list_nonterminal(path):
            try:
                current = (
                    operation
                    if operation.result is not None
                    else claim_operation(path, operation.operation_id)
                )
                if current is None:
                    continue
                if current.status == "validating":
                    if hooks.before_commit is not None:
                        await hooks.before_commit(operation.operation_id)
                    current = commit_draft(
                        path, operation.operation_id, current.last_event_id
                    )
                if current.result is not None:
                    if hooks.after_commit is not None:
                        await hooks.after_commit(operation.operation_id)
                    transition_operation(path, operation.operation_id, "complete")
            except asyncio.CancelledError:
                raise
            except Exception:  # noqa: BLE001 — supervised worker boundary records unexpected failures safely
                transition_operation(path, operation.operation_id, "failed")
