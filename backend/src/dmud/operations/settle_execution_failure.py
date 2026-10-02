from pathlib import Path

from dmud.operations.execution_failure import ExecutionFailure
from dmud.operations.get_operation import get_operation
from dmud.operations.models import Operation
from dmud.operations.transition_operation import transition_operation


def settle_execution_failure(path: Path, failure: ExecutionFailure) -> Operation:
    """Finish committed delivery or fail only the original uncommitted attempt; e.g. settle_execution_failure(path, failure)."""
    operation = get_operation(path, failure.operation_id)
    if operation.result is not None:
        return transition_operation(path, operation.operation_id, "complete")
    return transition_operation(
        path, operation.operation_id, "failed", failure.expected_event_id
    )
