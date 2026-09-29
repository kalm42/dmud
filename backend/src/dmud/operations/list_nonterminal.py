import logging
from contextlib import closing
from pathlib import Path

from pydantic import ValidationError

from dmud.operations.models import Operation, OperationError
from dmud.operations.read_operation import read_operation
from dmud.platform.sqlite.connect_database import connect_database


def list_nonterminal(path: Path) -> list[Operation]:
    """Read durable work independently of any in-memory queue; e.g. list_nonterminal(path)."""
    with closing(connect_database(path)) as db, db:
        db.execute("BEGIN")
        rows = db.execute(
            "SELECT operation_id FROM operations WHERE json_extract(resource, '$.status') IN ('accepted', 'validating', 'committed') ORDER BY rowid"
        ).fetchall()
        operations: list[Operation] = []
        for row in rows:
            try:
                operation = read_operation(db, row[0])
            except ValidationError, OperationError:
                logging.getLogger(__name__).warning(
                    "Unavailable operation excluded from work scan."
                )
                continue
            if operation.status in ("accepted", "validating", "committed"):
                operations.append(operation)
        return operations
