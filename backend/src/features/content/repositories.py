from datetime import datetime, timezone

from fastapi import HTTPException
from sqlalchemy import select, create_engine

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession

from features.content.interfaces import (
    PostRepositoryInterface,
    PlaylistRepositoryInterface,
    CategoryRepositoryInterface,
    TagRepositoryInterface,
)

from features.content.models import Post, Playlist, Category, Tag
from features.content.schemas import PostCreate, PostUpdate, PlaylistCreate, CategoryCreate, TagCreate


class PostRepository(PostRepositoryInterface):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, admin_id: int, post_create: PostCreate) -> Post:
        try:
            post = Post(
                title=post_create.title,
                content=post_create.content,
                author_id=admin_id,
                category_id=post_create.category_id,
                playlist_id=post_create.playlist_id,
            )
            self.session.add(post)
            await self.session.commit()
            await self.session.refresh(post)
            return post
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=f"Database error: {e}")

    async def update(self, admin_id: int, post_id: int, post_update: PostUpdate) -> Post:
        pass

    async def get_post_by_id(self, post_id: int) -> Post:
        query = select(Post).filter(Post.id == post_id)
        result = await self.session.execute(query)
        post = result.scalar()
        if not post:
            raise HTTPException(status_code=404, detail='Post not found')
        return post

    async def get_posts(self):
        result = await self.session.execute(select(Post))
        posts = result.scalars().all()
        return posts

    async def get_post(self, post_id: int):
        return await self.get_post_by_id(post_id=post_id)

    async def delete(self, post_id: int):
        pass


class PlaylistRepository(PlaylistRepositoryInterface):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_playlists(self):
        result = await self.session.execute(select(Playlist))
        playlists = result.scalars().all()
        return playlists

    async def get_playlist(self, playlist_id: int):
        result = await self.session.execute(select(Playlist).filter(Playlist.id == playlist_id))
        playlist = result.scalar()
        return playlist

    async def create(self, admin_id: int, playlist_create: PlaylistCreate) -> Playlist:
        playlist = Playlist(
            title=playlist_create.title,
            author_id=admin_id,
            created_at=datetime.now(timezone.utc)
        )
        self.session.add(playlist)
        await self.session.commit()
        await self.session.refresh(playlist)
        return playlist

    async def update(self, admin_id: int, post_id: int, playlist_update):
        pass

    async def delete_playlist(self, admin_id:int, playlist_id: int):
        pass

    async def delete_playlist_post(self, playlist_id: int, post_id: int):
        pass


class CategoryRepository(CategoryRepositoryInterface):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_categories(self):
        result = await self.session.execute(select(Category))
        categories = result.scalars().all()
        return categories

    async def create(self, admin_id: int, category_create: CategoryCreate) -> Category:
        category = Category(
            name=category_create.name,
            author=admin_id,
            create_at=datetime.now(timezone.utc)
        )
        self.session.add(category)
        await self.session.commit()
        await self.session.refresh(category)
        return category

    async def update(self, admin_id:int, category_id: int):
        pass

    async def delete(self, admin_id: int, category_id: int):
        pass


class TagRepository(TagRepositoryInterface):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_tags(self):
        result = await self.session.execute(select(Tag))
        tags = result.scalars().all()
        return tags

    async def create(self, admin_id: int, tag_create: TagCreate) -> Tag:
        tag = Tag(
            name=tag_create.name,
            author_id=admin_id,
            create_at=datetime.now(timezone.utc),
        )
        self.session.add(tag)
        await self.session.commit()
        await self.session.refresh(tag)
        return tag

    async def update(self, admin_id: int, tag_id: int):
        pass

    async def delete(self, admin_id: int, tag_id: int):
        pass

