from abc import ABC, abstractmethod


class PostRepositoryInterface(ABC):
    """Abstract method for Post"""
    @abstractmethod
    async def create(self, admin_id: int, post_create):
        pass

    @abstractmethod
    async def update(self, admin_id: int, post_id: int, post_update):
        pass

    @abstractmethod
    async def delete(self, post_id: int):
        pass

    @abstractmethod
    async def get_posts(self):
        pass

    @abstractmethod
    async def get_post(self, post_id: int):
        pass


class PlaylistRepositoryInterface(ABC):
    """Abstract method for Playlist"""
    @abstractmethod
    async def create(self, admin_id: int, playlist_create):
        pass

    @abstractmethod
    async def update(self, admin_id: int, post_id: int, playlist_update):
        pass

    @abstractmethod
    async def delete_playlist(self, admin_id:int, playlist_id: int):
        pass

    @abstractmethod
    async def delete_playlist_post(self, playlist_id: int, post_id: int):
        pass

    @abstractmethod
    async def get_playlists(self):
        pass

    @abstractmethod
    async def get_playlist(self, playlist_id: int):
        pass

class CategoryRepositoryInterface(ABC):
    """Abstract method for Category"""
    @abstractmethod
    async def create(self, admin_id: int, category_create):
        pass

    @abstractmethod
    async def update(self, admin_id:int, category_id: int):
        pass

    @abstractmethod
    async def delete(self, admin_id: int, category_id: int):
        pass

    @abstractmethod
    async def get_categories(self):
        pass


class TagRepositoryInterface(ABC):
    """Abstract method for Tag"""
    @abstractmethod
    async def create(self, admin_id: int, tag_create):
        pass

    @abstractmethod
    async def update(self, admin_id: int, tag_id: int):
        pass

    @abstractmethod
    async def delete(self, admin_id: int, tag_id: int):
        pass

    @abstractmethod
    async def get_tags(self):
        pass