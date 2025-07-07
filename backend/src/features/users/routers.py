from fastapi import APIRouter, Depends

from features.auth.oauth2 import get_current_user
from features.users.schamas import UserAuth, UserBase
from features.users.services import UserServices, get_user_services

user_app = APIRouter(prefix="/users", tags=["Users"])


@user_app.post("/login/", response_model=UserBase)
async def create_user(
        user_auth: UserAuth,
        services: UserServices = Depends(get_user_services),
):
    return await services.create(user_auth=user_auth)


@user_app.get(f"/profile/me/")
async def get_profile(
        current_user: UserBase = Depends(get_current_user)
):
    return await current_user


@user_app.get("/")
async def get_users(
    services: UserServices = Depends(get_user_services)
):
    return await services.get_users()
    
    
@user_app.get("/{user_id}/")
async def get_user_profile(user_id: int, services: UserServices = Depends(get_user_services)):
    return await services.get_user_profile(user_id=user_id)


