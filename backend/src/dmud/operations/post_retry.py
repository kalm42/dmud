from pathlib import Path

from fastapi import Request

from dmud.operations.models import Operation, RecoveryCommand
from dmud.operations.recover_operation import recover_operation


async def post_retry(
    operationId: str, payload: RecoveryCommand, request: Request
) -> Operation:
    """Retry supported uncommitted work under its original subject; e.g. POST operation/retry."""
    path: Path = request.app.state.database_path
    operation = recover_operation(path, operationId, payload, "retry")
    request.app.state.wake.set()
    return operation
