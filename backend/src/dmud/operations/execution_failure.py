from dataclasses import dataclass


@dataclass
class ExecutionFailure(Exception):
    """Identify the failed attempt without exposing infrastructure error details."""

    operation_id: str
    expected_event_id: int
