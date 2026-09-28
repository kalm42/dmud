import sqlite3

from dmud.operations.models import Operation, OperationEvent


def write_event(db: sqlite3.Connection, operation: Operation) -> None:
    """Persist snapshot and ordered event in the caller's transaction; e.g. write_event(db, operation)."""
    event = OperationEvent(event_id=operation.last_event_id, operation=operation)
    db.execute(
        "UPDATE operations SET resource = ? WHERE operation_id = ?",
        (operation.model_dump_json(by_alias=True), operation.operation_id),
    )
    db.execute(
        "INSERT INTO operation_events VALUES (?, ?, ?)",
        (operation.operation_id, event.event_id, event.model_dump_json(by_alias=True)),
    )
