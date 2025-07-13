from fastapi import APIRouter, Depends

from features import Admin
from features.auth.oauth2 import get_current_admin
from features.content.dependencies import get_tag_services
from features.content.schemas import TagBase, TagCreate
from features.content.services import TagServices

tag_app = APIRouter(tags=['Tags'])


@tag_app.get("/tags/", response_model=list[TagBase])
async def get_tags(
        services: TagServices = Depends(get_tag_services)
):
    return await services.get_tags()


@tag_app.post("/tags/", response_model=TagCreate)
async def create_tag(
        tag_create: TagCreate,
        current_admin: Admin = Depends(get_current_admin),
        services: TagServices = Depends(get_tag_services)
):
    return await services.create(admin_id=current_admin.id, tag_create=tag_create)

