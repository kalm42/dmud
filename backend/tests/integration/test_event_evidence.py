import json
import sqlite3
from pathlib import Path

import pytest

from dmud.operations.accept_operation import accept_operation
from dmud.operations.commit_draft import commit_draft
from dmud.operations.get_events import get_events
from dmud.operations.get_operation import get_operation
from dmud.operations.models import OperationError
from dmud.operations.transition_operation import transition_operation
from dmud.platform.sqlite.initialize_database import initialize_database
from dmud.session_zero.models import CreateSessionZeroDraft


@pytest.mark.parametrize(
    "damage",
    [
        "request_identity",
        "commit_boundary",
        "envelope_cursor",
        "committed_result",
        "lifecycle_order",
    ],
)
def test_event_replay_rejects_contradictory_historical_evidence(
    tmp_path: Path, damage: str
) -> None:
    path = initialize_database(tmp_path)
    operation = accept_operation(
        path,
        CreateSessionZeroDraft(requestId="req_00000000-0000-4000-8000-000000000045"),
    )
    transition_operation(path, operation.operation_id, "validating")
    commit_draft(path, operation.operation_id)
    with sqlite3.connect(path) as db:
        event = json.loads(
            db.execute(
                "SELECT resource FROM operation_events WHERE event_id = 1"
            ).fetchone()[0]
        )
        if damage == "request_identity":
            event["operation"]["requestId"] = "req_00000000-0000-4000-8000-000000000046"
        elif damage == "commit_boundary":
            event["operation"]["status"] = "complete"
        elif damage == "envelope_cursor":
            event["eventId"] = 2
        else:
            committed = json.loads(
                db.execute(
                    "SELECT resource FROM operation_events WHERE event_id = 3"
                ).fetchone()[0]
            )
            event["operation"] = committed["operation"]
            event["operation"]["lastEventId"] = 1
            if damage == "committed_result":
                event["operation"]["committedRevision"] = 99
                event["operation"]["result"]["committedRevision"] = 99
        db.execute(
            "UPDATE operation_events SET resource = ? WHERE event_id = 1",
            (json.dumps(event),),
        )

    with pytest.raises(OperationError, match="event_history_unavailable"):
        get_events(path, operation.operation_id, 0)


def test_operation_read_rejects_a_contradictory_latest_cursor(tmp_path: Path) -> None:
    path = initialize_database(tmp_path)
    operation = accept_operation(
        path,
        CreateSessionZeroDraft(requestId="req_00000000-0000-4000-8000-000000000047"),
    )
    with sqlite3.connect(path) as db:
        db.execute(
            "UPDATE operation_events SET resource = json_set(resource, '$.eventId', 2)"
        )

    with pytest.raises(OperationError, match="event_history_unavailable"):
        get_operation(path, operation.operation_id)


def test_event_replay_validates_transition_from_the_resume_cursor(
    tmp_path: Path,
) -> None:
    path = initialize_database(tmp_path)
    operation = accept_operation(
        path,
        CreateSessionZeroDraft(requestId="req_00000000-0000-4000-8000-000000000057"),
    )
    transition_operation(path, operation.operation_id, "validating")
    transition_operation(path, operation.operation_id, "interrupted")
    with sqlite3.connect(path) as db:
        db.execute(
            "UPDATE operation_events SET resource = json_set(resource, '$.operation.status', 'accepted') WHERE event_id = 2"
        )

    with pytest.raises(OperationError, match="event_history_unavailable"):
        get_events(path, operation.operation_id, 1)
