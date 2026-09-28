import sqlite3

from fastapi import Request
from starlette.responses import JSONResponse

from dmud.operations.models import OperationError
from dmud.operations.render_problem import render_problem


async def problem_response(request: Request, error: Exception) -> JSONResponse:
    """Translate boundary failures to secret-free RFC 9457 data; e.g. app.add_exception_handler(error, problem_response)."""
    if isinstance(error, OperationError):
        problem = error.problem
    elif isinstance(error, sqlite3.OperationalError) and error.sqlite_errorcode in (
        sqlite3.SQLITE_BUSY,
        sqlite3.SQLITE_LOCKED,
    ):
        problem = OperationError("application_data_busy", 409).problem
    else:
        problem = OperationError("operation_unavailable", 503).problem
    return render_problem(problem)
