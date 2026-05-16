from dataclasses import dataclass, field
from uuid import UUID, uuid4

from datetime import datetime, timezone


@dataclass
class CategoryEntity:
    """
    Категория для логической группировки постов.
    Позволяет классифицировать контент по тематическим разделам.
    """

    id: UUID
    name: str
    created_at: datetime = field(default_factory=datetime.now(timezone.utc))

    @staticmethod
    def create(name: str) -> "CategoryEntity":
        if not name.strip():
            raise ValueError("Category name cannot be empty")
        return CategoryEntity(id=uuid4(), name=name)
    
    def update(self, name: str) -> None:
        if not name or not name.strip():
            raise ValueError("Category name cannot be empty")
        self.name = name.strip()

