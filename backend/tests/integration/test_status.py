import sqlite3

import pytest
from fastapi.testclient import TestClient

from dmud.main import create_app


def test_status_returns_ready_without_exposing_secret(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    monkeypatch.setenv("DMUD_LLM_API_KEY", "canary-private-credential-123")
    client = TestClient(create_app())

    response = client.get("/api/status")

    assert response.status_code == 200
    assert response.json() == {"status": "ready"}
    assert "canary-private-credential-123" not in response.text
    assert "canary-private-credential-123" not in str(capsys.readouterr())


def test_startup_rejects_unsupported_sqlite() -> None:
    with pytest.raises(RuntimeError, match="SQLite 3.37.0"):
        create_app(sqlite_version=(3, 36, 0))


def test_startup_accepts_installed_sqlite() -> None:
    client = TestClient(create_app(sqlite_version=sqlite3.sqlite_version_info))

    assert client.get("/api/status").status_code == 200
