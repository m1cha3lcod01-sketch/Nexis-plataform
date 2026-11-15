"""Configuración central cargada desde variables de entorno."""

from pathlib import Path

from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    """Opciones de la API y variables preparadas para Supabase."""

    app_name: str = Field(default="NEXIS API", validation_alias="NEXIS_APP_NAME")
    app_description: str = Field(
        default="API central de NEXIS",
        validation_alias="NEXIS_APP_DESCRIPTION",
    )
    app_version: str = Field(default="1.0.0", validation_alias="NEXIS_APP_VERSION")

    supabase_url: str | None = None
    supabase_anon_key: SecretStr | None = None

    model_config = SettingsConfigDict(
        env_file=BACKEND_DIR / ".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
        extra="ignore",
    )


settings = Settings()
