from contextlib import closing
from pathlib import Path

from dmud.operations.models import (
    DraftResult,
    Operation,
    RecoveryCapability,
)
from dmud.operations.read_operation import read_operation
from dmud.operations.write_event import write_event
from dmud.platform.sqlite.connect_database import connect_database
from dmud.session_zero.create_session_zero_draft import create_session_zero_draft
from dmud.session_zero.models import CreateSessionZeroDraft


def commit_draft(
    path: Path, operation_id: str, expected_event_id: int | None = None
) -> Operation:
    """Atomically commit draft, result, immutable evidence and status; e.g. commit_draft(path, id)."""
    with closing(connect_database(path)) as db, db:
        db.execute("BEGIN IMMEDIATE")
        operation = read_operation(db, operation_id)
        if (
            operation.result is not None
            or operation.status != "validating"
            or (
                expected_event_id is not None
                and operation.last_event_id != expected_event_id
            )
        ):
            return operation
        row = db.execute(
            "SELECT payload, payload_digest FROM operations WHERE operation_id = ?",
            (operation_id,),
        ).fetchone()
        CreateSessionZeroDraft.model_validate_json(row[0])
        draft = create_session_zero_draft(operation.subject, operation_id)
        result = DraftResult(subject=operation.subject, committed_revision=1)
        db.execute(
            "INSERT INTO session_zero_drafts VALUES (?, ?, ?, ?)",
            (draft.draft_id, 1, draft.model_dump_json(by_alias=True), operation_id),
        )
        db.execute(
            "INSERT INTO draft_commits VALUES (?, ?, ?, ?)",
            (operation_id, draft.draft_id, 1, row[1]),
        )
        db.execute(
            "INSERT INTO request_results VALUES (?, ?, ?, ?)",
            (
                operation.request_id,
                operation_id,
                draft.draft_id,
                result.model_dump_json(by_alias=True),
            ),
        )
        updated = operation.model_copy(
            update={
                "status": "committed",
                "commit_boundary": "draft",
                "committed_revision": 1,
                "result": result,
                "last_event_id": operation.last_event_id + 1,
                "recovery": RecoveryCapability(retry=False, cancel=False),
            }
        )
        write_event(db, updated)
        return updated
