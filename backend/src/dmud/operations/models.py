from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field
from pydantic.alias_generators import to_camel

RequestId = Annotated[
    str,
    Field(
        pattern=r"^req_[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$"
    ),
]
OperationStatus = Literal[
    "accepted", "validating", "committed", "complete", "failed", "interrupted"
]


class WireModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid", strict=True, alias_generator=to_camel, populate_by_name=True
    )


class RecoveryCommand(WireModel):
    schema_version: Literal[1] = 1
    request_id: RequestId
    expected_last_event_id: Annotated[int, Field(gt=0)]


class Subject(WireModel):
    kind: Literal["session_zero_draft"] = "session_zero_draft"
    draft_id: Annotated[str, Field(pattern=r"^draft_[0-9a-f-]{36}$")]


class RecoveryCapability(WireModel):
    retry: bool
    cancel: bool


class DraftResult(WireModel):
    subject: Subject
    commit_boundary: Literal["draft"] = "draft"
    committed_revision: Annotated[int, Field(gt=0)]


class Operation(WireModel):
    schema_version: Literal[1] = 1
    operation_id: Annotated[str, Field(pattern=r"^op_[0-9a-f-]{36}$")]
    request_id: RequestId
    subject: Subject
    status: OperationStatus
    commit_boundary: Literal["none", "draft"]
    committed_revision: Annotated[int, Field(gt=0)] | None
    last_event_id: Annotated[int, Field(gt=0)]
    recovery: RecoveryCapability
    result: DraftResult | None
    status_url: str
    events_url: str


class OperationEvent(WireModel):
    schema_version: Literal[1] = 1
    event_id: Annotated[int, Field(gt=0)]
    operation: Operation


ProblemCode = Literal[
    "invalid_request",
    "request_conflict",
    "operation_not_found",
    "operation_unavailable",
    "draft_not_committed",
    "draft_not_found",
    "draft_unavailable",
    "draft_already_committed",
    "event_history_unavailable",
    "invalid_event_cursor",
    "stale_event",
    "recovery_not_supported",
    "application_data_busy",
]
ProblemStatus = Literal[404, 409, 422, 503]


class Problem(WireModel):
    type: str
    title: str
    status: ProblemStatus
    detail: str
    code: ProblemCode
    classification: Literal["conflict", "invalid_input", "not_found", "unavailable"]
    instance: str
    correlation_id: str
    operation: Operation | None = None


class OperationError(Exception):
    """Carry a safe validated boundary problem without SQL or configuration details."""

    def __init__(
        self,
        code: ProblemCode,
        status: ProblemStatus = 409,
        operation: Operation | None = None,
    ):
        classification: Literal[
            "conflict", "invalid_input", "not_found", "unavailable"
        ] = "unavailable"
        if status == 409:
            classification = "conflict"
        elif status == 422:
            classification = "invalid_input"
        elif status == 404:
            classification = "not_found"
        self.problem = Problem(
            type=f"urn:dmud:problem:{code}",
            title=code.replace("_", " ").capitalize(),
            status=status,
            detail="Query the original request or operation to recover its authoritative status.",
            code=code,
            classification=classification,
            instance="urn:dmud:problem:pending",
            correlation_id="pending",
            operation=operation,
        )
        super().__init__(code)
