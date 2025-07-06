from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_async_session
from features.content.repositories import (PostRepository,
                                           PlaylistRepository,
                                           CategoryRepository,
                                           TagRepository)
from features.content.services import (PostServices,
                                       PlaylistServices,
                                       CategoryServices,
                                       TagServices)


async def get_post_services(
    session: AsyncSession = Depends(get_async_session)
) -> PostServices:
    post_repo = PostRepository(session=session)
    return PostServices(post_repo=post_repo)


async def get_playlist_services(
    session: AsyncSession = Depends(get_async_session)
) -> PlaylistServices:
    playlist_repo = PlaylistRepository(session=session)
    return PlaylistServices(playlist_repo=playlist_repo)


async def get_category_services(
    session: AsyncSession = Depends(get_async_session)
) -> CategoryServices:
    category_repo = CategoryRepository(session=session)
    return CategoryServices(category_repo=category_repo)


async def get_tag_services(
    session: AsyncSession = Depends(get_async_session)
) -> TagServices:
    tag_repo = TagRepository(session=session)
    return TagServices(tag_repo=tag_repo)
