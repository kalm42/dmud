from pathlib import Path

from fastapi import Request

from dmud.authored_content.content_result import ContentResult, ContentUnavailable
from dmud.authored_content.require_content import require_content
from dmud.operations.accept_operation import accept_operation
from dmud.operations.get_request_operation import get_request_operation
from dmud.operations.models import Operation
from dmud.platform.sqlite.run_database import run_database
from dmud.session_zero.models import CreateSessionZeroDraft


async def post_draft(payload: CreateSessionZeroDraft, request: Request) -> Operation:
    """Accept before waking the supervised command worker; e.g. POST /api/session-zero-drafts.

    Without valid content, only an already accepted request may still be replayed; a
    new request is refused with content_unavailable before anything is created.
    """
    path: Path = request.app.state.database_path
    content: ContentResult = request.app.state.content
    if isinstance(content, ContentUnavailable):
        accepted = await run_database(get_request_operation, path, payload.request_id)
        if accepted is None:
            require_content(content)
    try:
        return await run_database(accept_operation, path, payload)
    finally:
        request.app.state.wake.set()
