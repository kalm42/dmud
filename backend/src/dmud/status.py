from typing import Literal

from pydantic import BaseModel, ConfigDict


class StatusResponse(BaseModel):
    """Describe the read-only application readiness response; for example, StatusResponse(status='ready')."""

    model_config = ConfigDict(strict=True, extra="forbid")
    status: Literal["ready"]
