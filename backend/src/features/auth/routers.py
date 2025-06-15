from typing import Annotated

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from features.admin.services import get_admin_services
from features.auth.oauth2 import create_access_token
from features.auth.schemas import Token
from db.database import get_async_session
from features.auth.security import verify_password, verify_admin_data

auth_app = APIRouter(prefix='')


@auth_app.post('/token/')
async def get_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        session: AsyncSession = Depends(get_async_session),
) -> Token:
    if verify_admin_data(form_data.username, form_data.password):
        admin_service = await get_admin_services(session=session)
        admin = await admin_service.login(form_data.username)
        print(admin)
        if not verify_password(form_data.password, admin.password_hash):
            raise HTTPException(status_code=401, detail="Wrong password")
        access_token = create_access_token(
            data={
                "sub": admin.email,
                "is_admin": True
            })
        return Token(access_token=access_token, token_type="bearer")


    user = 'user' # здесь логику я не прописал, но потом допишу
    return user


