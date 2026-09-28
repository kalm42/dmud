from collections.abc import AsyncIterator
from pathlib import Path
from typing import Annotated

from fastapi import Depends, Request
from fastapi.sse import ServerSentEvent

from dmud.operations.event_cursor import event_cursor
from dmud.operations.stream_events import stream_events


async def read_events(
    operationId: str, request: Request, cursor: Annotated[int, Depends(event_cursor)]
) -> AsyncIterator[ServerSentEvent]:
    """Stream validated history after a preflight dependency; e.g. GET operation/events."""
    path: Path = request.app.state.database_path
    async for event in stream_events(path, operationId, cursor):
        yield event
