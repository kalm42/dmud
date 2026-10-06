import shutil
from pathlib import Path

import pytest

from dmud.platform.settings import REPOSITORY_CONTENT_DIRECTORY


@pytest.fixture(autouse=True)
def isolated_data(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("DMUD_APPLICATION_DATA_DIRECTORY", str(tmp_path / "application"))


@pytest.fixture
def content_copy(tmp_path: Path) -> Path:
    """An isolated, editable copy of the committed content package for broken-content tests."""
    destination = tmp_path / "content"
    shutil.copytree(REPOSITORY_CONTENT_DIRECTORY, destination)
    return destination
