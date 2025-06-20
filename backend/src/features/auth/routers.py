from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from features.auth.schemas import Token
from db.database import get_async_session
from features.auth.security import verify_admin_data
from features.auth.services import get_admin_token, get_user_token

auth_app = APIRouter(tags=["Auth"])


@auth_app.post('/token/')
async def get_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        session: AsyncSession = Depends(get_async_session),
) -> Token:
    if verify_admin_data(form_data.username, form_data.password):
        return await get_admin_token(form_data=form_data, session=session)
    return await get_user_token(form_data=form_data, session=session)


