from fastapi import APIRouter, Depends

from features import Admin
from features.auth.oauth2 import get_current_admin
from features.content.dependencies import get_post_services
from features.content.schemas import PostCreate, PostBase
from features.content.services import PostServices

post_app = APIRouter(tags=['Posts'])


@post_app.get("/posts/", response_model=PostBase)
async def get_posts(
        services: PostServices = Depends(get_post_services),
):
    return await services.get_posts()


@post_app.get("/posts/{post_id}", response_model=PostBase)
async def get_post(
        post_id: int,
        services: PostServices = Depends(get_post_services),
):
    return await services.get_post(post_id=post_id)


@post_app.post("/posts/", response_model=PostCreate)
async def update_post(
        post_create: PostCreate,
        current_admin: Admin = Depends(get_current_admin),
        services: PostServices = Depends(get_post_services),
):
    return await services.create(admin_id=current_admin.id, post_create=post_create)
