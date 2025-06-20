from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_async_session
from features.admin.services import get_admin_services
from features.auth.oauth2 import create_access_token
from features.auth.schemas import Token
from features.auth.security import verify_password
from features.users.services import get_user_services


async def get_admin_token(
        form_data: OAuth2PasswordRequestForm,
        session: AsyncSession = Depends(get_async_session),
):
    """Return admin access token"""
    admin_service = await get_admin_services(session=session)
    admin = await admin_service.login(email=form_data.username)
    if not verify_password(form_data.password, admin.password_hash):
        raise HTTPException(status_code=401, detail="Wrong password")
    access_token = create_access_token(
        data={
            "sub": admin.id,
            "email": admin.email,
            "is_admin": True,
        })
    return Token(access_token=access_token, token_type="bearer")


async def get_user_token(
        form_data: OAuth2PasswordRequestForm,
        session: AsyncSession = Depends(get_async_session),
):
    """Return admin access token"""
    user_services = await get_user_services(session=session)
    user = await user_services.login(email=form_data.username)
    if not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Wrong password")
    access_token = create_access_token(
        data={
            "sub": user.id,
            "email": user.email,
            "username": user.username,
        })
    return Token(access_token=access_token, token_type="bearer")