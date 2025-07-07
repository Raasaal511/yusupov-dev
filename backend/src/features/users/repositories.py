from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError, NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from features.auth.security import bcrypt_password
from features.users.interfaces import UserRepositoryInterface
from features.users.models import User
from features.users.schamas import UserAuth


class UserRepository(UserRepositoryInterface):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user_auth: UserAuth):
        try:
            user = User(
                username=user_auth.username,
                email=user_auth.email,
                password_hash=bcrypt_password(user_auth.password_hash),
            )
            if not user:
                raise HTTPException(status_code=404, detail='User not found')
            self.session.add(user)
            await self.session.commit()
            await self.session.refresh(user)
            return user
        except SQLAlchemyError:
            raise HTTPException(status_code=500, detail="Wrong when create user")

    async def get_user_by_id(self, user_id: int) -> User:
        query = select(User).where(User.id == user_id)
        result = await self.session.execute(query)
        user = result.scalars().first()
        if not user:
            raise HTTPException(status_code=404, detail='User not found')
        return user

    async def get_user_by_email(self, email:str) -> User:
        query = select(User).where(User.email == email)
        result = await self.session.execute(query)
        user = result.scalars().first()
        if not user:
            raise HTTPException(status_code=404, detail='User not found')
        return user

    async def get_user(self, user_id: int):
        try:
            user = await self.get_user_by_id(user_id=user_id)
            return user
        except NoResultFound:
            raise HTTPException(status_code=404, detail='User not found')
        except SQLAlchemyError as e:
            raise HTTPException(
                status_code=500,
                detail=f"Database error: {str(e)}"
            )

    async def get_users(self):
        result = await self.session.execute(select(User))
        users = result.scalars().all()
        return users
        
    async def login(self, email: str):
        try:
            user = self.get_user_by_email(email=email)
        except NoResultFound:
            raise HTTPException(status_code=404, detail='User not found')
        except SQLAlchemyError as e:
            raise HTTPException(
                status_code=500,
                detail=f"Database error: {str(e)}"
            )

    async def get_profile(self,):
        ...
