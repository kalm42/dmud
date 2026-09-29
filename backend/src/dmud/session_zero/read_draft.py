from pathlib import Path

from fastapi import Request

from dmud.platform.sqlite.run_database import run_database
from dmud.session_zero.get_session_zero_draft import get_session_zero_draft
from dmud.session_zero.models import SessionZeroDraft


async def read_draft(draftId: str, request: Request) -> SessionZeroDraft:
    """Expose only committed draft material; e.g. GET /api/session-zero-drafts/{id}."""
    path: Path = request.app.state.database_path
    return await run_database(get_session_zero_draft, path, draftId)
