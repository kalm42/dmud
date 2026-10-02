from dmud.operations.models import Operation, OperationError


def validate_operation_snapshot(operation: Operation) -> Operation:
    """Check pure lifecycle and commitment invariants for current or historical data; e.g. validate_operation_snapshot(operation)."""
    committed = operation.commit_boundary == "draft"
    if (
        committed != (operation.status in ("committed", "complete"))
        or committed != (operation.result is not None)
        or committed != (operation.committed_revision is not None)
        or operation.recovery.retry != (operation.status in ("failed", "interrupted"))
        or operation.recovery.cancel != (operation.status in ("accepted", "validating"))
        or operation.status_url != f"/api/operations/{operation.operation_id}"
        or operation.events_url != f"{operation.status_url}/events"
    ):
        raise OperationError("operation_unavailable", 503)
    if operation.result is not None and (
        operation.result.subject != operation.subject
        or operation.result.committed_revision != operation.committed_revision
    ):
        raise OperationError("operation_unavailable", 503)
    return operation
