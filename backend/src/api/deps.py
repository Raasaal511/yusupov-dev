from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.infrastructure.database import get_async_session
from backend.src.infrastructure.repositories.content import CategoryRepository
from backend.src.application.content.services import CategoryService


async def get_category_service(
    session: AsyncSession = Depends(get_async_session),
) -> CategoryService:
    repo = CategoryRepository(session=session)
    return CategoryService(category_repo=repo, session=session)
