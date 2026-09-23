from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Validate backend-only configuration; for example, Settings()."""

    model_config = SettingsConfigDict(env_prefix="DMUD_", extra="ignore")
    llm_api_key: SecretStr | None = None
