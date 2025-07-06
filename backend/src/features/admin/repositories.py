
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.exc import NoResultFound, SQLAlchemyError

from sqlalchemy.ext.asyncio import AsyncSession

from features.admin.exceptions import AdminNotFoundError
from features.admin.models import Admin
from features.auth.security import bcrypt_password
from features.admin.schemas import AdminAuth
from features.admin.interfaces import AdminRepositoryInterface


class AdminRepository(AdminRepositoryInterface):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, admin_auth: AdminAuth) -> Admin:
        try:
            admin = Admin(
                email=admin_auth.email,
                first_name=admin_auth.first_name,
                last_name=admin_auth.last_name,
                password_hash=bcrypt_password(admin_auth.password_hash)
            )
            self.session.add(admin)
            await self.session.commit()
            await self.session.refresh(admin)
            return admin
        except SQLAlchemyError as e:
            raise HTTPException(status_code=500, detail=f"Database error: {e}")

    async def get_admin_by_id(self, admin_id: int) -> Admin:
        query = select(Admin).where(Admin.id == admin_id)
        result = await self.session.execute(query)
        admin = result.scalars().first()
        if not admin:
            raise HTTPException(status_code=404, detail="Amdin not found or you not have permission")
        return admin

    async def get_admin_by_email(self, email: str) -> Admin:
        query = select(Admin).where(Admin.email == email)
        result = await self.session.execute(query)
        admin = result.scalars().first()
        if not admin:
            raise HTTPException(status_code=404, detail="Admin not found or you not have permission")
        return admin

    async def get_admin(self, admin_id: int) -> Admin:
        try:
            admin = await self.get_admin_by_id(admin_id=admin_id)
            return admin
        except NoResultFound:
            raise AdminNotFoundError(status_code=404, detail=f"Admin not found")
        except SQLAlchemyError as e:
            raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
            )

    async def login(self, email: str) -> Admin:
        try:
            admin = await self.get_admin_by_email(email=email)
            return admin
        except NoResultFound:
            raise AdminNotFoundError(status_code=404, detail=f"Admin not found")
        except SQLAlchemyError as e:
            raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
            )
