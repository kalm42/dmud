from pathlib import Path
from typing import Annotated

from fastapi import Header, Request

from dmud.operations.get_events import get_events
from dmud.operations.models import OperationError
from dmud.platform.sqlite.run_database import run_database


async def event_cursor(
    operationId: str,
    request: Request,
    last_event_id: Annotated[str | None, Header()] = None,
) -> int:
    """Validate cursor before starting SSE; e.g. GET events with Last-Event-ID: 2."""
    path: Path = request.app.state.database_path
    if last_event_id is not None and (
        not last_event_id.isascii()
        or not last_event_id.isdigit()
        or len(last_event_id) > 15
    ):
        raise OperationError("invalid_event_cursor", 409)
    cursor = int(last_event_id or "0")
    await run_database(get_events, path, operationId, cursor)
    return cursor
