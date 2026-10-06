import sqlite3
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from dmud.main import create_app
from dmud.platform.settings import Settings

REQUEST = {"requestId": "req_00000000-0000-4000-8000-000000000044"}


def broken_settings(tmp_path: Path) -> Settings:
    return Settings(
        application_data_directory=tmp_path / "data",
        content_directory=tmp_path / "absent-content",
    )


def row_counts(database: Path) -> dict[str, int]:
    with sqlite3.connect(database) as db:
        tables = [
            row[0]
            for row in db.execute(
                "SELECT name FROM sqlite_master WHERE type = 'table' AND name NOT LIKE 'sqlite_%' AND name != 'schema_migrations'"
            )
        ]
        return {
            table: db.execute(f'SELECT count(*) FROM "{table}"').fetchone()[0]
            for table in tables
        }


class TestContentUnavailable:
    def test_application_keeps_serving(self, tmp_path: Path) -> None:
        with TestClient(create_app(settings=broken_settings(tmp_path))) as client:
            assert client.get("/api/status").status_code == 200

    def test_new_game_returns_typed_content_unavailable_problem(
        self, tmp_path: Path
    ) -> None:
        with TestClient(create_app(settings=broken_settings(tmp_path))) as client:
            response = client.post("/api/session-zero-drafts", json=REQUEST)
        problem = response.json()
        assert response.status_code == 503
        assert response.headers["content-type"] == "application/problem+json"
        assert (problem["code"], problem["classification"]) == (
            "content_unavailable",
            "unavailable",
        )
        assert problem["operation"] is None

    def test_problem_detail_is_factual_and_path_free(self, tmp_path: Path) -> None:
        with TestClient(create_app(settings=broken_settings(tmp_path))) as client:
            response = client.post("/api/session-zero-drafts", json=REQUEST)
        assert "nothing was started" in response.json()["detail"]
        assert str(tmp_path) not in response.text

    def test_rejected_new_game_creates_nothing(self, tmp_path: Path) -> None:
        settings = broken_settings(tmp_path)
        with TestClient(create_app(settings=settings)) as client:
            client.post("/api/session-zero-drafts", json=REQUEST)
        counts = row_counts(tmp_path / "data" / "dmud.sqlite3")
        assert counts and set(counts.values()) == {0}

    def test_accepted_request_still_replays_after_content_fails(
        self, tmp_path: Path
    ) -> None:
        data = tmp_path / "data"
        with TestClient(
            create_app(settings=Settings(application_data_directory=data))
        ) as client:
            accepted = client.post("/api/session-zero-drafts", json=REQUEST).json()
        with TestClient(create_app(settings=broken_settings(tmp_path))) as client:
            replay = client.post("/api/session-zero-drafts", json=REQUEST)
        assert replay.status_code == 202
        assert replay.json()["operationId"] == accepted["operationId"]

    def test_invalid_content_package_is_refused_like_missing_content(
        self, tmp_path: Path, content_copy: Path
    ) -> None:
        (content_copy / "worlds/brackenford/npcs/ivo.yaml").unlink()
        settings = Settings(
            application_data_directory=tmp_path / "data",
            content_directory=content_copy,
        )
        with TestClient(create_app(settings=settings)) as client:
            response = client.post("/api/session-zero-drafts", json=REQUEST)
        assert response.json()["code"] == "content_unavailable"


class TestContentLoading:
    def test_valid_content_lets_new_game_proceed(self) -> None:
        with TestClient(create_app()) as client:
            response = client.post("/api/session-zero-drafts", json=REQUEST)
        assert response.status_code == 202

    def test_constructing_and_exporting_the_app_reads_no_content(
        self, tmp_path: Path
    ) -> None:
        app = create_app(settings=broken_settings(tmp_path))
        app.openapi()
        assert not hasattr(app.state, "content")


@pytest.mark.parametrize(
    "relative,text",
    [
        ("bad.yaml", "kind: npc\nname: 2026-99-99\n"),
        ("bad.yaml", 'kind: npc\nname: !!int ""\n'),
        ("bad.yaml", 'kind: npc\nname: !!bool "maybe"\n'),
        ("bad.yaml", 'kind: npc\nname: !!timestamp "bogus"\n'),
        ("bad.yaml", "kind: npc\nloop: &loop [*loop]\n"),
        (
            "manifest.yaml",
            'kind: manifest\ncontent_schema_version: 1\npackage_id: package:brackenford-p0\npackage_version: "'
            + "1" * 4301
            + '.0.0"\n',
        ),
    ],
)
def test_malformed_content_keeps_new_game_recoverable(
    tmp_path: Path, relative: str, text: str
) -> None:
    content = tmp_path / "content"
    content.mkdir()
    (content / relative).write_text(text)
    settings = Settings(
        application_data_directory=tmp_path / "data", content_directory=content
    )

    with TestClient(create_app(settings=settings)) as client:
        response = client.post("/api/session-zero-drafts", json=REQUEST)

    assert response.status_code == 503
    assert response.json()["code"] == "content_unavailable"
