from domain.content.entities import CategoryEntity
from infrastructure.models.content import Category


class CategoryMapper:
    @staticmethod
    def to_entity(model: Category) -> CategoryEntity:
        return CategoryEntity(
            id=model.id,
            name=model.name,
            created_at=model.created_at,
        )

    @staticmethod
    def to_model(entity: CategoryEntity) -> Category:
        return Category(
            id=entity.id,
            name=entity.name,
            created_at=entity.created_at,
        )
