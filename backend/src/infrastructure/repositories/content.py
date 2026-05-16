from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete

from infrastructure.mappers.cotent import CategoryMapper
from domain.content.entities import CategoryEntity
from domain.content.repositories import ICategoryRepository
from infrastructure.models.content import Category


class CategoryRepository(ICategoryRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, category: CategoryEntity) -> CategoryEntity:
        model = CategoryMapper.to_model(category)
        self.session.add(model)
        await self.session.flush()
        await self.session.refresh(model)
        return CategoryMapper.to_entity(model)

    async def get_by_name(self, category_name: str) -> CategoryEntity | None:
        stmt = select(Category).where(Category.name == category_name)
        result = await self.session.execute(stmt)
        model = result.scalar_one_or_none()
        if not model:
            return None
        return CategoryMapper.to_entity(model)

    async def get_by_id(self, category_id: UUID) -> Category | None:
        stmt = select(Category).where(Category.id == category_id)
        result = await self.session.execute(stmt)
        model = result.scalar_one_or_none()
        if not model:
            return None
        return CategoryMapper.to_entity(model)

    async def list(self) -> list[CategoryEntity]:
        stmt = select(Category)
        result = await self.session.execute(stmt)
        models = result.scalars().all()
        return [CategoryMapper.to_entity(m) for m in models]

    async def update(self, category: CategoryEntity) -> None:
        stmt = select(Category).where(Category.id == category.id)
        result = await self.session.execute(stmt)
        model = result.scalar_one()
        model.name = category.name
        await self.session.flush()
        return CategoryMapper.to_entity(model)

    async def delete(self, category: CategoryEntity) -> None:
        stmt = delete(Category).where(Category.id == category.id)
        await self.session.execute(stmt)
        await self.session.commit()
