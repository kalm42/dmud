from contextlib import closing
from pathlib import Path

from dmud.operations.models import OperationError, OperationEvent
from dmud.operations.read_operation import read_operation
from dmud.platform.sqlite.connect_database import connect_database


def get_events(path: Path, operation_id: str, cursor: int) -> list[OperationEvent]:
    """Replay validated durable history strictly after a cursor; e.g. get_events(path, id, 2)."""
    with closing(connect_database(path)) as db, db:
        operation = read_operation(db, operation_id)
        if cursor < 0 or cursor > operation.last_event_id:
            raise OperationError("invalid_event_cursor", 409, operation)
        rows = db.execute(
            "SELECT event_id, resource FROM operation_events WHERE operation_id = ? AND event_id > ? ORDER BY event_id",
            (operation_id, cursor),
        ).fetchall()
        events = [OperationEvent.model_validate_json(row[1]) for row in rows]
        if [event.event_id for event in events] != list(
            range(cursor + 1, operation.last_event_id + 1)
        ):
            raise OperationError("event_history_unavailable", 503, operation)
        if any(
            event.operation.operation_id != operation_id
            or event.operation.subject != operation.subject
            or event.operation.last_event_id != event.event_id
            for event in events
        ):
            raise OperationError("event_history_unavailable", 503, operation)
        return events
