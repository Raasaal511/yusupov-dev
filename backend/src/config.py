import os

from dotenv import load_dotenv
from pydantic import computed_field
from pydantic_settings import BaseSettings

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")


class DBSettings(BaseSettings):
    """Настройки базы данных"""

    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str
    postgres_port: str

    @computed_field
    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"


class AdminSettings(BaseSettings):
    """Конфигурация базы данных"""

    admin_first_name: str
    admin_last_name: str
    admin_email: str
    admin_password: str

    @computed_field
    @property
    def full_name(self) -> str:
        return f"{self.admin_first_name} {self.admin_last_name}"


db_settings = DBSettings()
admin_settings = AdminSettings()


print(db_settings.url)
print(admin_settings.full_name)
