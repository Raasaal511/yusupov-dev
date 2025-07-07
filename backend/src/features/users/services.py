from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_async_session
from features.users.interfaces import UserRepositoryInterface
from features.users.repositories import UserRepository
from features.users.schamas import UserAuth, UserBase


class UserServices:
    def __init__(self, user_repo: UserRepositoryInterface):
        self.user_repo = user_repo

    async def create(self, user_auth: UserAuth):
        user_create = await self.user_repo.create(user_auth=user_auth)
        return UserAuth.model_validate(user_create, from_attributes=True)

    async def get_user(self, user_id: int):
        user = await self.user_repo.get_user(user_id=user_id)
        return UserBase.model_validate(user, from_attributes=True)
    
    async def get_users(self):
        users = await self.user_repo.get_users()
        return users

    async def login(self, email: str):
        return await self.user_repo.login(email=email)

    async def get_user_profile(self, user_id: int):
        user = await self.user_repo.get_user(user_id=user_id)
        return UserBase.model_validate(user, from_attributes=True)


async def get_user_services(
    session: AsyncSession = Depends(get_async_session)
) -> UserServices:
    user_repo = UserRepository(session=session)
    return  UserServices(user_repo=user_repo)

