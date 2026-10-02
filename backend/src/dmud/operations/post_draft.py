from pathlib import Path

from fastapi import Request

from dmud.operations.accept_operation import accept_operation
from dmud.operations.models import Operation
from dmud.platform.sqlite.run_database import run_database
from dmud.session_zero.models import CreateSessionZeroDraft


async def post_draft(payload: CreateSessionZeroDraft, request: Request) -> Operation:
    """Accept before waking the supervised command worker; e.g. POST /api/session-zero-drafts."""
    path: Path = request.app.state.database_path
    try:
        return await run_database(accept_operation, path, payload)
    finally:
        request.app.state.wake.set()
