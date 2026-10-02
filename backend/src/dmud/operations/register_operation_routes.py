import sqlite3

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.sse import EventSourceResponse
from pydantic import ValidationError

from dmud.operations.invalid_request import invalid_request
from dmud.operations.models import Operation, OperationError, OperationEvent, Problem
from dmud.operations.post_cancel import post_cancel
from dmud.operations.post_draft import post_draft
from dmud.operations.post_retry import post_retry
from dmud.operations.problem_response import problem_response
from dmud.operations.read_events import read_events
from dmud.operations.read_status import read_status
from dmud.session_zero.models import SessionZeroDraft
from dmud.session_zero.read_draft import read_draft


def register_operation_routes(app: FastAPI) -> None:
    """Compose thin operation routes and explicit problem contracts; e.g. register_operation_routes(app)."""
    problems: dict[int | str, dict[str, object]] = {
        status: {
            "model": Problem,
            "content": {
                "application/problem+json": {
                    "schema": {"$ref": "#/components/schemas/Problem"}
                }
            },
        }
        for status in (404, 409, 422, 503)
    }
    app.add_exception_handler(OperationError, problem_response)
    app.add_exception_handler(sqlite3.Error, problem_response)
    app.add_exception_handler(ValidationError, problem_response)
    app.add_exception_handler(RequestValidationError, invalid_request)
    app.add_api_route(
        "/api/session-zero-drafts",
        post_draft,
        methods=["POST"],
        response_model=Operation,
        status_code=202,
        operation_id="createSessionZeroDraft",
        responses=problems,
    )
    app.add_api_route(
        "/api/session-zero-drafts/{draftId}",
        read_draft,
        methods=["GET"],
        response_model=SessionZeroDraft,
        operation_id="getSessionZeroDraft",
        responses=problems,
    )
    app.add_api_route(
        "/api/operations/{operationId}",
        read_status,
        methods=["GET"],
        response_model=Operation,
        operation_id="getOperation",
        responses=problems,
    )
    app.add_api_route(
        "/api/operations/{operationId}/events",
        read_events,
        methods=["GET"],
        response_class=EventSourceResponse,
        operation_id="getOperationEvents",
        responses={
            **problems,
            200: {
                "model": OperationEvent,
                "content": {
                    "text/event-stream": {
                        "schema": {"$ref": "#/components/schemas/OperationEvent"}
                    }
                },
                "description": "Ordered versioned operation events. Resume strictly after Last-Event-ID. Invalid or future cursors return a problem; query status before reconnecting with a valid cursor.",
            },
        },
    )
    app.add_api_route(
        "/api/operations/{operationId}/cancel",
        post_cancel,
        methods=["POST"],
        response_model=Operation,
        operation_id="cancelOperation",
        responses=problems,
    )
    app.add_api_route(
        "/api/operations/{operationId}/retry",
        post_retry,
        methods=["POST"],
        response_model=Operation,
        status_code=202,
        operation_id="retryOperation",
        responses=problems,
    )
