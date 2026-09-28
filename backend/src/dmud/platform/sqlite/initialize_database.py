import sqlite3
from pathlib import Path

from dmud.platform.require_sqlite import require_sqlite
from dmud.platform.sqlite.connect_database import connect_database


def initialize_database(directory: Path, migrations: Path | None = None) -> Path:
    """Apply ordered atomic migrations before serving; e.g. initialize_database(data_dir)."""
    require_sqlite(sqlite3.sqlite_version_info)
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / "dmud.sqlite3"
    db = connect_database(path)
    try:
        version = db.execute("PRAGMA user_version").fetchone()[0]
        files = sorted(
            (migrations or Path(__file__).parent / "migrations").glob("*.sql")
        )
        if version > len(files):
            raise RuntimeError("Application data schema is newer than supported.")
        for number, migration in enumerate(files, 1):
            if number <= version:
                continue
            db.executescript(
                "BEGIN IMMEDIATE;\n"
                + migration.read_text()
                + f"\nINSERT INTO schema_migrations VALUES ({number});\nPRAGMA user_version = {number};\nCOMMIT;"
            )
    except sqlite3.Error:
        if db.in_transaction:
            db.rollback()
        raise RuntimeError("Application data migration unavailable.") from None
    finally:
        db.close()
    return path
