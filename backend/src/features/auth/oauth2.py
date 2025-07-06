from typing import Annotated

import jwt

from fastapi import HTTPException

from datetime import datetime, timezone
from datetime import timedelta

from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError

from config.security import SECRET_KEY
from features.admin.services import AdminServices, get_admin_services
from features.auth.schemas import TokenData
from features.users.services import get_user_services, UserServices

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
        """Create access token with lifetime 15 minute"""
        encode = data.copy()
        if expires_delta:
            expire = datetime.now(timezone.utc) + expires_delta
        else:
            expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        encode.update({"exp": expire})
        encode_jwt = jwt.encode(encode, SECRET_KEY, algorithm="HS256")
        return  encode_jwt


async def get_current_admin(
        token: Annotated[str, Depends(oauth2_scheme)],
        services: AdminServices = Depends(get_admin_services)
):
    """Return current admin"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        admin_id = payload.get("sub")
        if admin_id is None:
            raise HTTPException(status_code=401, detail="Not Authenticated")
        token_admin_data = TokenData(id=admin_id)
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail=f"Could not validate credentials")

    admin = await services.get_admin(admin_id=token_admin_data.id)
    if admin is None:
        raise HTTPException(status_code=401, detail=f"Admin is not found")
    return admin


async def get_current_user(
        token: Annotated[str, Depends(oauth2_scheme)],
        services: UserServices = Depends(get_user_services),
):
    """Return current user"""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Not Authenticated")
        token_user_data= TokenData(id=user_id)
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")

    user = await services.get_user(user_id=token_user_data.id)
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    return user
