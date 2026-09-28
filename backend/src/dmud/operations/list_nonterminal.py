from contextlib import closing
from pathlib import Path

from dmud.operations.models import Operation
from dmud.operations.read_operation import read_operation
from dmud.platform.sqlite.connect_database import connect_database


def list_nonterminal(path: Path) -> list[Operation]:
    """Read durable work independently of any in-memory queue; e.g. list_nonterminal(path)."""
    with closing(connect_database(path)) as db, db:
        rows = db.execute(
            "SELECT operation_id FROM operations WHERE json_extract(resource, '$.status') IN ('accepted', 'validating', 'committed') ORDER BY rowid"
        ).fetchall()
        return [
            operation
            for row in rows
            if (operation := read_operation(db, row[0])).status
            in ("accepted", "validating", "committed")
        ]
