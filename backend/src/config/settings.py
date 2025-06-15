import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_PATH = Path(__file__).resolve().parent.parent.parent.parent / ".env"

load_dotenv(dotenv_path=ENV_PATH)


class DBSettings(BaseSettings):
    """Настройки базы данных"""
    db_user: str
    db_password: str
    db_name: str
    db_host: str
    db_port: str
    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file='.env',
        env_prefix="DB_",
        extra="ignore"
    )
    @computed_field
    @property
    def db_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


class AdminSettings(BaseSettings):
    admin_email: str
    admin_password: str
    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file='.env',
        env_prefix="ADMIN_",
        extra="ignore",
    )


db_settings = DBSettings(
    db_user=os.getenv("DB_USER"),
    db_password=os.getenv("DB_PASSWORD"),
    db_name=os.getenv("DB_NAME"),
    db_host=os.getenv("DB_HOST"),
    db_port=os.getenv("DB_PORT"),
)

admin_settings = AdminSettings(
    admin_email=os.getenv("ADMIN_EMAIL"),
    admin_password=os.getenv("ADMIN_PASSWORD"),
)

