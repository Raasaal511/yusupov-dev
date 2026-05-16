from uuid import UUID, uuid4
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from domain.content.entities import CategoryEntity
from domain.content.repositories import ICategoryRepository

from content.dto import CategoryDTO, CreateCategoryDTO, UpdateCategoryDTO
from content.exceptions import CategoryAlreadyExists, CategoryNotFoundError


class CategoryService:
    def __init__(
        self,
        category_repo: ICategoryRepository,
        session: AsyncSession,
    ):
        self.category_repo = category_repo
        self.session = session

    async def create(self, dto: CreateCategoryDTO) -> CategoryDTO:
        """
        Создание категории по валидации dto
        dto: CreateCategoryDTO
        dto: Валидация создания категории
        """
        category = await self.category_repo.get_by_name(name=dto.name)

        if category:
            raise CategoryAlreadyExists("Category already exists")
        new_category = CategoryEntity(id=uuid4(), name=dto.name)
        created_category = await self.category_repo.create(category=new_category)
        await self.session.commit()
        return self._to_dto(created_category)

    async def get_by_id(self, category_id: UUID) -> CategoryDTO:
        """Получения категории по id."""
        category = await self._get_or_not_found(category_id=category_id)
        return self._to_dto(category)

    async def get_by_name(self, name: str) -> CategoryDTO:
        """Получения категории по name."""
        category = await self.category_repo.get_by_name(name=name)

        if not category:
            raise CategoryNotFoundError("Category not found")
        return self._to_dto(category)

    async def get_all(self, skip: int = 0, limit: int = 10) -> List[CategoryDTO]:
        """Получение всех категорий."""
        categories = await self.category_repo.get_all(skip=skip, limit=limit)
        return [self._to_dto(category) for category in categories]

    async def update(self, category_id: UUID, dto: UpdateCategoryDTO) -> CategoryDTO:
        """Обновление категории."""
        category = await self._get_or_not_found(category_id=category_id)

        if dto.name and dto.name != category.name:
            existing = await self.category_repo.get_by_name(dto.name)

            if existing and existing.id != category.id:
                raise CategoryAlreadyExists("Category already exists")
            category.name = dto.name

        updated_category = await self.category_repo.update(category=category)
        await self.session.commit()
        return self._to_dto(updated_category)

    async def delete(self, category_id: UUID) -> None:
        """Удаления категории."""
        await self._get_or_not_found(category_id=category_id)
        await self.category_repo.delete(id=category_id)
        await self.session.commit()

    def _to_dto(self, model: CategoryEntity) -> CategoryDTO:
        """Преоброзование модель в DTO"""
        return CategoryDTO.model_validate(model)

    async def _get_or_not_found(self, category_id: UUID) -> CategoryEntity:
        """Получает товар по id если такого тавара нет то вызывает исключение."""
        category = await self.category_repo.get_by_id(id=category_id)

        if not category:
            raise CategoryNotFoundError("Category not found")
        return category
