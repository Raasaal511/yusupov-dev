from abc import ABC, abstractmethod


class UserRepositoryInterface(ABC):

    @abstractmethod
    async def create(self, user_auth):
        pass

    @abstractmethod
    async def get_user(self, user_id: int):
        pass

    @abstractmethod
    async def login(self, email: str):
        pass

    @abstractmethod
    async def get_profile(self):
        pass