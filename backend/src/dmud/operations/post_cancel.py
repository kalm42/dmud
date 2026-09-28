from pathlib import Path

from fastapi import Request

from dmud.operations.models import Operation, RecoveryCommand
from dmud.operations.recover_operation import recover_operation


async def post_cancel(
    operationId: str, payload: RecoveryCommand, request: Request
) -> Operation:
    """Request cooperative cancellation at the commit boundary; e.g. POST operation/cancel."""
    path: Path = request.app.state.database_path
    return recover_operation(path, operationId, payload, "cancel")
