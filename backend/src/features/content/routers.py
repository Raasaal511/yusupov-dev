from fastapi import APIRouter
from fastapi.params import Depends

from features.admin.schemas import AdminInfo
from features.auth.oauth2 import get_current_admin
from features.content.schemas import PostUpdate, PostCreate
from features.content.services import PostServices
from features.content.dependencies import get_post_services

content_app = APIRouter(prefix="/content", tags=["content"])


@content_app.post('/posts/create/')
async def update_post(
        post_create: PostCreate,
        current_admin: AdminInfo = Depends(get_current_admin),
        services: PostServices = Depends(get_post_services),
):
    return await services.create(admin_id=current_admin.id, post_create=post_create)


@content_app.put('/posts/update/{post_id}/')
async def update_post(
        post_id: int,
        post_update: PostUpdate,
        current_admin: AdminInfo = Depends(get_current_admin),
        services: PostServices = Depends(get_post_services),
):
    return await services.update(admin_id=current_admin.id, post_id=post_id, post_update=post_update)
