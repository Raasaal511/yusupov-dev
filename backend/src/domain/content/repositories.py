from abc import ABC, abstractmethod
from uuid import UUID

from src.domain.content.entities import CategoryEntity


# class IPostRepository(ABC):
#     """
#     Интерфейс для работы с постами.
#     Гарантирование постов что могут выплнять crud-реализацию
#     и возможность фильтрации по
#     """
#     @abstractmethod
#     def create(self, post: Post) -> None:
#         pass

#     @abstractmethod
#     def get_by_id(self, id: UUID) -> Post:
#         pass

#     @abstractmethod
#     def get_all(self, skip: int = 0, limit: int = 10) -> list[Post]:
#         pass

#     @abstractmethod
#     def get_all_by_category_id(self, category_id: UUID, skip: int, limit: int) -> list[Post]:
#         pass

#     @abstractmethod
#     def get_all_by_tag_id(self, tag_id: UUID, skip: int, limit: int) -> list[Post]:
#         pass

#     @abstractmethod
#     def get_all_by_playlist_id(self, playlist_id: UUID, skip: int, limit: int) -> list[Post]:
#         pass

#     @abstractmethod
#     def update(self, id: UUID) -> None:
#         pass

#     @abstractmethod
#     def delete(self, id: UUID) -> None:
#         pass

#     @abstractmethod
#     def increment_view(self, post_id: UUID) -> None:
#         """Увеличить счетчик просмотров (без записи в View)"""
#         pass


class ICategoryRepository(ABC):
    @abstractmethod
    async def create(self, category: CategoryEntity) -> None:
        pass

    @abstractmethod
    async def get_by_name(self, name: str) -> CategoryEntity:
        pass

    @abstractmethod
    async def get_by_id(self, id: UUID) -> CategoryEntity:
        pass

    @abstractmethod
    async def list(self) -> list[CategoryEntity]:
        pass

    @abstractmethod
    async def update(self, category: CategoryEntity) -> CategoryEntity:
        pass

    @abstractmethod
    async def delete(self, category: CategoryEntity) -> None:
        pass

# class ITagRepository(ABC):
#     @abstractmethod
#     def create(self, tag: Tag) -> None:
#         pass

#     @abstractmethod
#     def get_by_id(self, id: UUID) -> Tag:
#         pass

#     @abstractmethod
#     def get_all(self, skip: int, limit: int) -> list[Tag]:
#         pass

#     @abstractmethod
#     def update(self, id: UUID) -> None:
#         pass

#     @abstractmethod
#     def delete(self, id: UUID) -> None:
#         pass

# class IPlaylistRepository(ABC):
#     @abstractmethod
#     def create(self, playlist: Playlist) -> None:
#         pass

#     @abstractmethod
#     def get_by_id(self, id: UUID) -> Playlist:
#         pass

#     @abstractmethod
#     def get_all(self, skip: int, limit: int) -> list[Playlist]:
#         pass

#     @abstractmethod
#     def update(self, id: UUID) -> None:
#         pass

#     @abstractmethod
#     def delete(self, id: UUID) -> None:
#         pass
