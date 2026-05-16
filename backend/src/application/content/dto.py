from uuid import UUID
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class CategoryDTO(BaseModel):
    id: UUID
    name: str
    created_at: datetime


class CreateCategoryDTO(BaseModel):
    name: str = Field(min_length=3, max_length=155)
    model_config = ConfigDict(from_attributes=True)


class UpdateCategoryDTO(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=155)
