from uuid import UUID

from pydantic import BaseModel, ConfigDict


class CategoryBase(BaseModel):
    name: str


class CreateCategoryRequest(CategoryBase):
    pass


class UpdateCategoryRequest(BaseModel):
    name: str | None


class CategoryResponse(BaseModel):
    id: UUID
    model_config = ConfigDict(from_attributes=True)
    