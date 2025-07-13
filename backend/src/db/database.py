from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncAttrs, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from config.settings import db_settings

DB_URL = db_settings.db_url

async_engine = create_async_engine(DB_URL)
async_sessionmaker = async_sessionmaker(
    async_engine,
    expire_on_commit=False,
)


class Base(AsyncAttrs, DeclarativeBase):
    pass


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_sessionmaker() as session:
        yield session
