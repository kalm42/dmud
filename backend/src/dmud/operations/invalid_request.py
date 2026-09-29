from pathlib import Path

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, ConfigDict, Field, ValidationError
from starlette.responses import JSONResponse

from dmud.operations.get_request_operation import get_request_operation
from dmud.operations.models import OperationError, RequestId
from dmud.operations.render_problem import render_problem
from dmud.platform.sqlite.run_database import run_database


class CreationIdentity(BaseModel):
    """Validate only duplicate lookup identity; remaining invalid input never enters domain code."""

    model_config = ConfigDict(extra="ignore", strict=True)
    request_id: RequestId = Field(alias="requestId")


async def invalid_request(request: Request, error: Exception) -> JSONResponse:
    """Reject secret-free input, with conflict for changed accepted requests; e.g. invalid_request(request, error)."""
    problem = OperationError("invalid_request", 422).problem
    if request.url.path == "/api/session-zero-drafts" and isinstance(
        error, RequestValidationError
    ):
        try:
            identity = CreationIdentity.model_validate(error.body)
        except ValidationError:
            identity = None
        if identity is not None:
            path: Path = request.app.state.database_path
            operation = await run_database(
                get_request_operation, path, identity.request_id
            )
            if operation is not None:
                problem = OperationError(
                    "request_conflict", operation=operation
                ).problem
    return render_problem(problem)
