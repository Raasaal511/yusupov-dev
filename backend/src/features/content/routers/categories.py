from fastapi import APIRouter, Depends

from features import Admin
from features.auth.oauth2 import get_current_admin
from features.content.dependencies import get_category_services
from features.content.repositories import CategoryRepository
from features.content.schemas import CategoryBase, CategoryCreate
from features.content.services import CategoryServices

category_app = APIRouter(tags=['Category'])


@category_app.get("/categories/", response_model=list[CategoryBase])
async def get_categories(
        services: CategoryRepository = Depends(get_category_services)
):
    return await services.get_categories()


@category_app.post("/categories/", response_model=CategoryBase)
async def create_category(
        category_create: CategoryCreate,
        current_admin: Admin = Depends(get_current_admin),
        services: CategoryServices = Depends(get_category_services),
):
    return await services.create(admin_id=current_admin.id, category_create=category_create)

