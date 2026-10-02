from contextlib import closing
from pathlib import Path

from dmud.operations.models import Operation
from dmud.operations.read_operation import read_operation
from dmud.operations.write_event import write_event
from dmud.platform.sqlite.connect_database import connect_database


def claim_operation(path: Path, operation_id: str) -> Operation | None:
    """Claim one accepted attempt transactionally across workers; e.g. claim_operation(path, id)."""
    with closing(connect_database(path)) as db, db:
        db.execute("BEGIN IMMEDIATE")
        operation = read_operation(db, operation_id)
        if operation.status != "accepted":
            return None
        claimed = operation.model_copy(
            update={
                "status": "validating",
                "last_event_id": operation.last_event_id + 1,
            }
        )
        write_event(db, claimed)
        return claimed
