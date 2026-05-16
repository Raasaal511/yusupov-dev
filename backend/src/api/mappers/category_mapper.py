from domain.content.entities import CategoryEntity
from api.schemas.content import CategoryResponse


def to_response(category: CategoryEntity) -> CategoryResponse:
    return CategoryResponse(
        id=category.id,
        name=category.name,
        created_at=category.created_at,
    )
