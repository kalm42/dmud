from contextlib import closing
from pathlib import Path

from dmud.operations.models import Operation
from dmud.operations.read_operation import read_operation
from dmud.platform.sqlite.connect_database import connect_database


def get_operation(path: Path, operation_id: str) -> Operation:
    """Read status without scheduling work; e.g. get_operation(path, operation_id)."""
    with closing(connect_database(path)) as db, db:
        return read_operation(db, operation_id)
