import sqlite3
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from dmud.main import create_app
from dmud.platform.settings import Settings


def test_application_construction_does_not_open_data(tmp_path: Path) -> None:
    data = tmp_path / "data"
    create_app(settings=Settings(application_data_directory=data)).openapi()
    assert not data.exists()


def test_lifespan_creates_only_strict_scoped_tables(tmp_path: Path) -> None:
    settings = Settings(application_data_directory=tmp_path)
    with TestClient(create_app(settings=settings)) as client:
        assert client.get("/api/status").status_code == 200
    with sqlite3.connect(tmp_path / "dmud.sqlite3") as db:
        tables = db.execute("PRAGMA table_list").fetchall()
        owned = {row[1] for row in tables if not row[1].startswith("sqlite_")}
        assert owned == {
            "schema_migrations",
            "session_zero_drafts",
            "operations",
            "operation_events",
            "request_results",
            "draft_commits",
            "recovery_commands",
        }
        assert all(row[5] == 1 for row in tables if row[1] in owned)
    with TestClient(create_app(settings=settings)):
        pass
    with sqlite3.connect(tmp_path / "dmud.sqlite3") as db:
        assert db.execute("SELECT count(*) FROM schema_migrations").fetchone()[0] == 1


def test_unsupported_sqlite_does_not_create_directory(tmp_path: Path) -> None:
    data = tmp_path / "unopened"
    with pytest.raises(RuntimeError, match="SQLite 3.37.0"):
        create_app(
            sqlite_version=(3, 36, 0),
            settings=Settings(application_data_directory=data),
        )
    assert not data.exists()


def test_failed_migration_rolls_back_all_schema(tmp_path: Path) -> None:
    from dmud.platform.sqlite.initialize_database import initialize_database

    migrations = tmp_path / "migrations"
    migrations.mkdir()
    (migrations / "0001.sql").write_text(
        "CREATE TABLE schema_migrations (version INTEGER PRIMARY KEY) STRICT; CREATE TABLE partial (id INTEGER) STRICT; INVALID SQL;"
    )
    with pytest.raises(RuntimeError, match="migration unavailable"):
        initialize_database(tmp_path / "data", migrations)
    with sqlite3.connect(tmp_path / "data" / "dmud.sqlite3") as db:
        assert (
            db.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
            == []
        )


def test_newer_schema_is_rejected_without_mutation(tmp_path: Path) -> None:
    from dmud.platform.sqlite.initialize_database import initialize_database

    path = initialize_database(tmp_path)
    with sqlite3.connect(path) as db:
        db.execute("PRAGMA user_version = 99")
    with pytest.raises(RuntimeError, match="newer than supported"):
        initialize_database(tmp_path)
    with sqlite3.connect(path) as db:
        assert db.execute("PRAGMA user_version").fetchone()[0] == 99
