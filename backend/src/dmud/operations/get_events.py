from contextlib import closing
from itertools import pairwise
from pathlib import Path

from pydantic import ValidationError

from dmud.operations.legal_transition import legal_transition
from dmud.operations.models import OperationError, OperationEvent
from dmud.operations.read_operation import read_operation
from dmud.operations.validate_operation_snapshot import validate_operation_snapshot
from dmud.platform.sqlite.connect_database import connect_database


def get_events(path: Path, operation_id: str, cursor: int) -> list[OperationEvent]:
    """Replay validated durable history strictly after a cursor; e.g. get_events(path, id, 2)."""
    with closing(connect_database(path)) as db, db:
        db.execute("BEGIN")
        operation = read_operation(db, operation_id)
        if cursor < 0 or cursor > operation.last_event_id:
            raise OperationError("invalid_event_cursor", 409, operation)
        first_event_id = max(1, cursor)
        rows = db.execute(
            "SELECT event_id, resource FROM operation_events WHERE operation_id = ? AND event_id >= ? ORDER BY event_id",
            (operation_id, first_event_id),
        ).fetchall()
        try:
            events = [OperationEvent.model_validate_json(row[1]) for row in rows]
            for event in events:
                validate_operation_snapshot(event.operation)
        except ValidationError, OperationError:
            raise OperationError("event_history_unavailable", 503, operation) from None
        if [event.event_id for event in events] != list(
            range(first_event_id, operation.last_event_id + 1)
        ):
            raise OperationError("event_history_unavailable", 503, operation)
        if any(
            event.operation.operation_id != operation_id
            or event.operation.request_id != operation.request_id
            or event.operation.subject != operation.subject
            or event.operation.last_event_id != event.event_id
            or (
                event.operation.result is not None
                and event.operation.result != operation.result
            )
            or row[0] != event.event_id
            for row, event in zip(rows, events, strict=True)
        ):
            raise OperationError("event_history_unavailable", 503, operation)
        if first_event_id == 1 and events and events[0].operation.status != "accepted":
            raise OperationError("event_history_unavailable", 503, operation)
        if any(
            not legal_transition(previous.operation.status, following.operation.status)
            for previous, following in pairwise(events)
        ):
            raise OperationError("event_history_unavailable", 503, operation)
        return [event for event in events if event.event_id > cursor]
