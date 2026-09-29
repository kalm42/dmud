import importlib
import sqlite3
import threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from dmud.main import create_app
from dmud.operations.accept_operation import accept_operation
from dmud.operations.commit_draft import commit_draft
from dmud.operations.get_operation import get_operation
from dmud.operations.transition_operation import transition_operation
from dmud.platform.settings import Settings
from dmud.platform.sqlite.connect_database import connect_database
from dmud.platform.sqlite.initialize_database import initialize_database
from dmud.session_zero.models import CreateSessionZeroDraft


@pytest.mark.parametrize("reader_name", ["get_operation", "get_events"])
def test_status_reads_preserve_a_snapshot_during_a_concurrent_commit(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, reader_name: str
) -> None:
    path = initialize_database(tmp_path)
    with sqlite3.connect(path) as db:
        db.execute("PRAGMA journal_mode = WAL")
    operation = accept_operation(
        path,
        CreateSessionZeroDraft(requestId="req_00000000-0000-4000-8000-000000000048"),
    )
    transition_operation(path, operation.operation_id, "validating")
    module = importlib.import_module(f"dmud.operations.{reader_name}")
    committed = False

    def traced_connection(database_path: Path) -> sqlite3.Connection:
        db = connect_database(database_path)

        def interleave(statement: str) -> None:
            nonlocal committed
            if "SELECT resource FROM request_results" in statement and not committed:
                committed = True
                commit_draft(path, operation.operation_id)

        db.set_trace_callback(interleave)
        return db

    # Schedule a real second-connection commit between the reader's evidence queries.
    monkeypatch.setattr(module, "connect_database", traced_connection)
    if reader_name == "get_operation":
        assert module.get_operation(path, operation.operation_id).status == "validating"
    else:
        assert [
            event.event_id
            for event in module.get_events(path, operation.operation_id, 0)
        ] == [1, 2]
    assert committed
    assert get_operation(path, operation.operation_id).status == "committed"


def test_status_remains_responsive_while_creation_waits_for_a_database_lock(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    module = importlib.import_module("dmud.operations.accept_operation")
    waiting = threading.Event()

    def traced_connection(database_path: Path) -> sqlite3.Connection:
        db = connect_database(database_path)
        db.set_trace_callback(
            lambda statement: waiting.set() if statement == "BEGIN IMMEDIATE" else None
        )
        return db

    # Observe the real adapter reaching a lock held by another real SQLite connection.
    monkeypatch.setattr(module, "connect_database", traced_connection)
    with (
        TestClient(
            create_app(settings=Settings(application_data_directory=tmp_path))
        ) as client,
        sqlite3.connect(tmp_path / "dmud.sqlite3") as blocker,
        ThreadPoolExecutor(max_workers=2) as executor,
    ):
        blocker.execute("BEGIN IMMEDIATE")
        creation = executor.submit(
            client.post,
            "/api/session-zero-drafts",
            json={"requestId": "req_00000000-0000-4000-8000-000000000049"},
        )
        try:
            assert waiting.wait(2)
            status = executor.submit(client.get, "/api/status").result(timeout=1)
            assert status.status_code == 200
        finally:
            blocker.rollback()
        assert creation.result(timeout=3).status_code == 202
