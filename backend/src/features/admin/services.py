from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_async_session
from features.admin.schemas import AdminAuth, AdminInfo, AdminBase, AdminLogIn

from features.admin.repositories import AdminRepository

from features.admin.interfaces import AdminRepositoryInterface


class AdminServices:
    def __init__(self, admin_repo: AdminRepositoryInterface):
        self.admin_repo = admin_repo

    async def create(self, admin_auth):
        admin_create = await self.admin_repo.create(admin_auth)
        return AdminAuth.model_validate(admin_create, from_attributes=True)

    async def get_admin(self, email: str):
        get_admin_repo = await self.admin_repo.get_admin(email=email)
        return AdminInfo.model_validate(get_admin_repo, from_attributes=True)

    async def login(self, email: str):
        admin = await self.admin_repo.get_admin(email)
        return admin

async def get_admin_services(
    session: AsyncSession = Depends(get_async_session)
) -> AdminServices:
    admin_repo = AdminRepository(session=session)

    return AdminServices(admin_repo=admin_repo)

