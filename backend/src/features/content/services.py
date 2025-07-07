from features.content.interfaces import (PostRepositoryInterface,
                                         PlaylistRepositoryInterface,
                                         CategoryRepositoryInterface,
                                         TagRepositoryInterface)
from features.content.schemas import (PostCreate,
                                      PlaylistCreate,
                                      CategoryCreate,
                                      TagCreate)


class PostServices:
    def __init__(self, post_repo: PostRepositoryInterface):
        self.post_repo = post_repo

    async def get_posts(self):
        posts = await self.post_repo.get_posts()
        return posts

    async def get_post(self, post_id: int):
        post = await self.get_post(post_id=post_id)
        return post

    async def create(self, admin_id: int, post_create: PostCreate) -> PostCreate:
        post = await self.post_repo.create(admin_id=admin_id, post_create=post_create)
        return post


class PlaylistServices:
    def __init__(self, playlist_repo: PlaylistRepositoryInterface):
        self.playlist_repo = playlist_repo

    async def get_playlists(self):
        playlists = await self.playlist_repo.get_playlists()
        return playlists

    async def get_playlist(self, playlist_id: int):
        playlist = await self.playlist_repo.get_playlist(playlist_id=playlist_id)
        return playlist

    async def create(self, admin_id: int, playlist_create: PlaylistCreate) -> PlaylistCreate:
        playlist = await self.playlist_repo.create(admin_id=admin_id, playlist_create=playlist_create)
        return playlist


class CategoryServices:
    def __init__(self, category_repo: CategoryRepositoryInterface):
        self.category_repo = category_repo

    async def get_categories(self):
        categories = await self.category_repo.get_categories()
        return categories

    async def create(self, admin_id: int, create_category: CategoryCreate):
        category_create = await self.category_repo.create(admin_id=admin_id, create_category=create_category)
        return category_create


class TagServices:
    def __init__(self, tag_repo: TagRepositoryInterface):
        self.tag_repo = tag_repo

    async def get_tags(self):
        tags = await self.tag_repo.get_tags()
        return tags

    def create(self, admin_id: int, tag_create: TagCreate):
        create_tag = self.tag_repo.create(admin_id=admin_id, tag_create=tag_create)
        return create_tag

