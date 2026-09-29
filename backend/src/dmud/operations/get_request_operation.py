from contextlib import closing
from pathlib import Path

from dmud.operations.models import Operation
from dmud.operations.read_operation import read_operation
from dmud.platform.sqlite.connect_database import connect_database


def get_request_operation(path: Path, request_id: str) -> Operation | None:
    """Resolve a logical request identity without allocating anything; e.g. get_request_operation(path, request_id)."""
    with closing(connect_database(path)) as db, db:
        db.execute("BEGIN")
        row = db.execute(
            "SELECT operation_id FROM operations WHERE request_id = ?", (request_id,)
        ).fetchone()
        return read_operation(db, row[0]) if row else None
