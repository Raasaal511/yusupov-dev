from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
    create_async_engine,
    AsyncAttrs,
    AsyncSession,
)
from sqlalchemy.orm import DeclarativeBase

from src.config import db_settings


async_engine = create_async_engine(url=db_settings.url)
async_sessionmaker = async_sessionmaker(
    async_engine,
    expire_on_commit=False,
)


class Base(AsyncAttrs, DeclarativeBase):
    pass


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_sessionmaker() as session:
        yield session
