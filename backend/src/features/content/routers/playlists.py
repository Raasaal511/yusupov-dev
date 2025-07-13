from fastapi import APIRouter, Depends

from features import Admin
from features.auth.oauth2 import get_current_admin
from features.content.dependencies import get_playlist_services
from features.content.schemas import PlaylistBase, PlaylistCreate
from features.content.services import PlaylistServices

playlist_app = APIRouter(tags=["Playlists"])


@playlist_app.get("/playlists/", response_model=list[PlaylistBase])
async def get_playlists(
        services: PlaylistServices = Depends(get_playlist_services),
):
    return await services.get_playlists()


@playlist_app.get("/playlists/{playlist_id}", response_model=PlaylistBase)
async def get_playlist(
        playlist_id: int,
        services: PlaylistServices = Depends(get_playlist_services),
):
    return await services.get_playlist(playlist_id=playlist_id)


@playlist_app.post("/playlists/", response_model=PlaylistBase)
async def create_playlist(
        playlist_create: PlaylistCreate,
        current_admin: Admin = Depends(get_current_admin),
        services: PlaylistServices = Depends(get_playlist_services)
):
    return await services.create(admin_id=current_admin.id, playlist_create=playlist_create)
