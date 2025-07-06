from abc import ABC, abstractmethod


class AdminRepositoryInterface(ABC):
    @abstractmethod
    async def create(self, admin_auth):
        pass

    @abstractmethod
    async def get_admin(self, admin_id):
        pass

    @abstractmethod
    async def login(self, email):
        pass