from pathlib import Path

import pytest


@pytest.fixture(autouse=True)
def isolated_data(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DMUD_APPLICATION_DATA_DIRECTORY", str(tmp_path / "application"))
