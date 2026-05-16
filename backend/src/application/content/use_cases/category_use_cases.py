from uuid import UUID

from domain.content.entities import CategoryEntity
from application.content.uow import UnitOfWork


class CreateCategoryUseCase:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def execute(self, name: str) -> CategoryEntity:
        if await self.uow.category.get_by_name(name=name):
            raise ValueError("Category already exists")

        category = CategoryEntity.create(name=name)

        await self.uow.category.create(category)
        await self.uow.commit()
        return category


class UpdateCategoryUseCase:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def execute(self, category_id: UUID, name: str) -> CategoryEntity:
        category: CategoryEntity = await self.uow.category.get_by_id(id=category_id)
        if not category:
            raise ValueError("Category not found")
        
        category.update(name=name)

        await self.uow.commit()
        return category
     

class DeleteCategoryUseCase:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    async def execute(self, category_id: UUID) -> None:
        category: CategoryEntity = await self.uow.category.get_by_id(id=category_id)
        if not category:
            raise ValueError("Category not found")
        
        await self.uow.category.delete(category)
        await self.uow.commit()
