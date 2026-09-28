from contextlib import closing
from pathlib import Path

from dmud.operations.models import OperationError
from dmud.operations.read_operation import read_operation
from dmud.platform.sqlite.connect_database import connect_database
from dmud.session_zero.models import SessionZeroDraft


def get_session_zero_draft(path: Path, draft_id: str) -> SessionZeroDraft:
    """Read committed content only; e.g. get_session_zero_draft(path, draft_id)."""
    with closing(connect_database(path)) as db, db:
        row = db.execute(
            "SELECT resource, revision, operation_id FROM session_zero_drafts WHERE draft_id = ?",
            (draft_id,),
        ).fetchone()
        if row is not None:
            draft = SessionZeroDraft.model_validate_json(row[0])
            if (
                draft.draft_id != draft_id
                or draft.draft_revision != row[1]
                or draft.active_operation_id != row[2]
            ):
                raise OperationError("draft_unavailable", 503)
            operation = read_operation(db, draft.active_operation_id)
            if (
                operation.result is None
                or operation.subject.draft_id != draft_id
                or operation.committed_revision != draft.draft_revision
            ):
                raise OperationError("draft_unavailable", 503)
            return draft
        reserved = db.execute(
            "SELECT operation_id FROM operations WHERE draft_id = ?", (draft_id,)
        ).fetchone()
        if reserved:
            raise OperationError(
                "draft_not_committed", 404, read_operation(db, reserved[0])
            )
        raise OperationError("draft_not_found", 404)
