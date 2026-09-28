import asyncio
from collections.abc import AsyncIterator
from pathlib import Path

from fastapi.sse import ServerSentEvent

from dmud.operations.get_events import get_events
from dmud.operations.get_operation import get_operation


async def stream_events(
    path: Path, operation_id: str, cursor: int
) -> AsyncIterator[ServerSentEvent]:
    """Stream without holding a database transaction or owning work; e.g. stream_events(path, id, 0)."""
    while True:
        events = get_events(path, operation_id, cursor)
        for event in events:
            yield ServerSentEvent(
                raw_data=event.model_dump_json(by_alias=True),
                event="operation",
                id=str(event.event_id),
            )
            cursor = event.event_id
        operation = get_operation(path, operation_id)
        if (
            operation.status in ("complete", "failed", "interrupted")
            and cursor == operation.last_event_id
        ):
            return
        await asyncio.sleep(0.05)
