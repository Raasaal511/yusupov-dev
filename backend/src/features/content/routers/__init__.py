from fastapi import APIRouter

from .posts import post_app
from .playlists import playlist_app
from .categories import category_app
from .tags import tag_app


content_app = APIRouter()

content_app.include_router(post_app)
content_app.include_router(category_app)
content_app.include_router(playlist_app)
content_app.include_router(tag_app)