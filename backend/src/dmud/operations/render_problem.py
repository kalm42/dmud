from uuid import uuid7

from starlette.responses import JSONResponse

from dmud.operations.models import Problem


def render_problem(problem: Problem) -> JSONResponse:
    """Attach safe correlation context at the HTTP boundary; e.g. render_problem(error.problem)."""
    correlation_id = "cor_" + str(uuid7())
    document = problem.model_copy(
        update={
            "correlation_id": correlation_id,
            "instance": f"urn:dmud:request:{correlation_id}",
        }
    )
    return JSONResponse(
        document.model_dump(mode="json", by_alias=True),
        status_code=document.status,
        media_type="application/problem+json",
    )
