from pathlib import Path

from pydantic import computed_field
from pydantic.v1 import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_PATH = Path(__file__).resolve().parent.parent.parent.parent / ".env"


class DBSettings(BaseSettings):
    """Настройки базы данных"""
    db_user: str
    db_password: str
    db_name: str
    db_host: str
    db_port: int
    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        env_prefix="DB_",
        extra="ignore"
    )

    @computed_field
    @property
    def db_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


db_settings = DBSettings()
