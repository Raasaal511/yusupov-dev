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
async def get_user(
        current_user: UserBase = Depends(get_current_user)
):
    return await current_user

