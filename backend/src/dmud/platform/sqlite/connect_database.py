import sqlite3
from pathlib import Path


def connect_database(path: Path) -> sqlite3.Connection:
    """Open one short-lived typed-adapter connection; e.g. connect_database(path)."""
    db = sqlite3.connect(path, timeout=5)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA foreign_keys = ON")
    db.execute("PRAGMA busy_timeout = 5000")
    return db
