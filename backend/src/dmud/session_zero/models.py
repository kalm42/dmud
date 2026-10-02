from typing import Annotated, Literal

from pydantic import Field

from dmud.operations.models import RequestId, WireModel


class SessionZeroDraft(WireModel):
    schema_version: Literal[1] = 1
    draft_id: Annotated[str, Field(pattern=r"^draft_[0-9a-f-]{36}$")]
    draft_revision: Annotated[int, Field(gt=0)]
    lifecycle: Literal["collecting"] = "collecting"
    active_operation_id: str


class CreateSessionZeroDraft(WireModel):
    schema_version: Literal[1] = 1
    request_id: RequestId
    command: Literal["create_session_zero_draft"] = "create_session_zero_draft"


class DraftRevisionCommand(WireModel):
    """Existing-draft commands require optimistic revision evidence; creation does not."""

    schema_version: Literal[1] = 1
    request_id: RequestId
    draft_id: Annotated[str, Field(pattern=r"^draft_[0-9a-f-]{36}$")]
    expected_draft_revision: Annotated[int, Field(gt=0)]
