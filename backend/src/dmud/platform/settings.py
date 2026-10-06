from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

REPOSITORY_CONTENT_DIRECTORY = Path(__file__).resolve().parents[4] / "content"


class Settings(BaseSettings):
    """Validate backend-only configuration; for example, Settings()."""

    model_config = SettingsConfigDict(env_prefix="DMUD_", extra="ignore")
    llm_api_key: SecretStr | None = None
    application_data_directory: Path = Path.home() / ".dmud"
    content_directory: Path = REPOSITORY_CONTENT_DIRECTORY
