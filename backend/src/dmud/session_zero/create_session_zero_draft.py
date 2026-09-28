from dmud.operations.models import Subject
from dmud.session_zero.models import SessionZeroDraft


def create_session_zero_draft(subject: Subject, operation_id: str) -> SessionZeroDraft:
    """Establish empty collecting material at initial revision one; e.g. create_session_zero_draft(subject, id)."""
    return SessionZeroDraft(
        draft_id=subject.draft_id, draft_revision=1, active_operation_id=operation_id
    )
