from abc import ABC, abstractmethod

from domain.content.repositories import ICategoryRepository


class UnitOfWork(ABC):
    category = ICategoryRepository

    @abstractmethod
    async def commit(self):
        pass

    @abstractmethod
    async def rollback(self):
        pass