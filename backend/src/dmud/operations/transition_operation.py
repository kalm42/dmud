from contextlib import closing
from pathlib import Path

from dmud.operations.legal_transition import legal_transition
from dmud.operations.models import Operation, OperationStatus, RecoveryCapability
from dmud.operations.read_operation import read_operation
from dmud.operations.write_event import write_event
from dmud.platform.sqlite.connect_database import connect_database


def transition_operation(
    path: Path, operation_id: str, target: OperationStatus
) -> Operation:
    """Serialize a legal non-commit transition; e.g. transition_operation(path, id, 'validating')."""
    with closing(connect_database(path)) as db, db:
        db.execute("BEGIN IMMEDIATE")
        operation = read_operation(db, operation_id)
        if target == "committed" or not legal_transition(operation.status, target):
            return operation
        updated = operation.model_copy(
            update={
                "status": target,
                "last_event_id": operation.last_event_id + 1,
                "recovery": RecoveryCapability(
                    retry=target in ("failed", "interrupted"),
                    cancel=target in ("accepted", "validating"),
                ),
            }
        )
        write_event(db, updated)
        return updated
