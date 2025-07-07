from fastapi import APIRouter
from fastapi.params import Depends

from features.admin.schemas import AdminInfo
from features.auth.oauth2 import get_current_admin
from features.content.repositories import CategoryRepository
from features.content.schemas import PostCreate, PlaylistBase, PlaylistCreate, CategoryBase
from features.content.services import PostServices, PlaylistServices
from features.content.dependencies import get_post_services, get_playlist_services, get_category_services

content_app = APIRouter(prefix="/content", tags=["Content"])


@content_app.get("/posts/")
async def get_posts(
        services: PostServices = Depends(get_post_services),
):
    return await services.get_posts()


@content_app.get("/posts/{post_id}")
async def get_posts(
        post_id: int,
        services: PostServices = Depends(get_post_services),
):
    return await services.get_post(post_id=post_id)


@content_app.post("/posts/")
async def update_post(
        post_create: PostCreate,
        current_admin: AdminInfo = Depends(get_current_admin),
        services: PostServices = Depends(get_post_services),
):
    return await services.create(admin_id=current_admin.id, post_create=post_create)


@content_app.get("/playlists/", response_model=list[PlaylistBase])
async def get_playlists(
        services: PlaylistServices = Depends(get_playlist_services),
):
    return await services.get_playlists()


@content_app.get("/playlists/{playlist_id}", response_model=PlaylistBase)
async def get_playlist(
        playlist_id: int,
        services: PlaylistServices = Depends(get_playlist_services),
):
    return await services.get_playlist(playlist_id=playlist_id)


@content_app.post("/playlists/", response_model=PlaylistBase)
async def create_playlist(
        playlist_create: PlaylistCreate,
        current_admin: AdminInfo = Depends(get_current_admin),
        services: PlaylistServices = Depends(get_playlist_services)
):
    return await services.create(admin_id=current_admin.id, playlist_create=playlist_create)


@content_app.get("/categories/", response_model=list[CategoryBase])
async def get_categories(
        services: CategoryRepository = Depends(get_category_services)
):
    return await services.get_categories()
