from pathlib import Path

from fastapi import Request

from dmud.operations.models import Operation, RecoveryCommand
from dmud.operations.recover_operation import recover_operation
from dmud.platform.sqlite.run_database import run_database


async def post_retry(
    operationId: str, payload: RecoveryCommand, request: Request
) -> Operation:
    """Retry supported uncommitted work under its original subject; e.g. POST operation/retry."""
    path: Path = request.app.state.database_path
    try:
        return await run_database(
            recover_operation, path, operationId, payload, "retry"
        )
    finally:
        request.app.state.wake.set()
