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
from features.auth.schemas import TokenAdminData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
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
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        admin_email = payload.get("sub")
        if admin_email is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
        token_admin_data = TokenAdminData(admin_email=admin_email)
    except InvalidTokenError as e:
        raise HTTPException(status_code=401, detail=f"Could not validate credentials: {e}")

    admin = services.get_admin(email=token_admin_data.admin_email)
    if admin is None:
        raise HTTPException(status_code=401, detail=f"Could not validate credentials")
    return admin
