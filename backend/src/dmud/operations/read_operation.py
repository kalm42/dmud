import sqlite3

from dmud.operations.models import (
    DraftResult,
    Operation,
    OperationError,
    OperationEvent,
)


def read_operation(db: sqlite3.Connection, operation_id: str) -> Operation:
    """Validate a durable snapshot and commit evidence; e.g. read_operation(db, operation_id)."""
    row = db.execute(
        "SELECT resource, request_id, draft_id FROM operations WHERE operation_id = ?",
        (operation_id,),
    ).fetchone()
    if row is None:
        raise OperationError("operation_not_found", 404)
    operation = Operation.model_validate_json(row[0])
    if (
        operation.operation_id != operation_id
        or operation.request_id != row[1]
        or operation.subject.draft_id != row[2]
    ):
        raise OperationError("operation_unavailable", 503)
    evidence = db.execute(
        "SELECT resource FROM request_results WHERE operation_id = ?", (operation_id,)
    ).fetchone()
    result = DraftResult.model_validate_json(evidence[0]) if evidence else None
    committed = operation.commit_boundary == "draft"
    if committed != (result is not None) or operation.result != result:
        raise OperationError("operation_unavailable", 503)
    if result is not None and (
        result.subject != operation.subject
        or result.committed_revision != operation.committed_revision
    ):
        raise OperationError("operation_unavailable", 503)
    if committed != (operation.status in ("committed", "complete")):
        raise OperationError("operation_unavailable", 503)
    if not committed and operation.committed_revision is not None:
        raise OperationError("operation_unavailable", 503)
    if operation.recovery.retry != (
        operation.status in ("failed", "interrupted")
    ) or operation.recovery.cancel != (operation.status in ("accepted", "validating")):
        raise OperationError("operation_unavailable", 503)
    latest = db.execute(
        "SELECT resource FROM operation_events WHERE operation_id = ? AND event_id = ?",
        (operation_id, operation.last_event_id),
    ).fetchone()
    if latest is None:
        raise OperationError("event_history_unavailable", 503)
    if OperationEvent.model_validate_json(latest[0]).operation != operation:
        raise OperationError("event_history_unavailable", 503)
    if result is not None:
        audit = db.execute(
            "SELECT draft_id, revision FROM draft_commits WHERE operation_id = ?",
            (operation_id,),
        ).fetchone()
        if (
            audit is None
            or audit[0] != operation.subject.draft_id
            or audit[1] != result.committed_revision
        ):
            raise OperationError("operation_unavailable", 503)
    return operation
