from dmud.status import StatusResponse


def get_status() -> StatusResponse:
    """Report readiness without configuration; for example, GET /api/status."""
    return StatusResponse(status="ready")
