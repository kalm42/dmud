from pathlib import Path

from fastapi import Request

from dmud.operations.get_operation import get_operation
from dmud.operations.models import Operation
from dmud.platform.sqlite.run_database import run_database


async def read_status(operationId: str, request: Request) -> Operation:
    """Return authoritative status independently of streaming; e.g. GET /api/operations/{id}."""
    path: Path = request.app.state.database_path
    return await run_database(get_operation, path, operationId)
