from fastapi import APIRouter

from posts import post_app
from playlists import playlist_app
from categories import category_app
from tags import tag_app


content = APIRouter()


content.include_router(post_app)
content.include_router(category_app)
content.include_router(playlist_app)
content.include_router(tag_app)