from fastapi import APIRouter
from fastapi.params import Depends

from features.admin.schemas import AdminAuth, AdminInfo
from features.admin.services import get_admin_services, AdminServices
from features.auth.oauth2 import get_current_admin

admin_app = APIRouter(prefix="/admin", tags=["Admin"])


@admin_app.post("/login/")
async def create_admin(
        admin_auth: AdminAuth,
        services: AdminServices = Depends(get_admin_services),
):
    return await services.create(admin_auth=admin_auth)


@admin_app.get("/profile/", response_model=AdminInfo)
async def get_admin(
        current_admin: AdminInfo = Depends(get_current_admin),
):
    return await current_admin