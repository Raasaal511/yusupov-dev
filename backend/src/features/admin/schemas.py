from typing import Self

from pydantic import BaseModel, model_validator, EmailStr

from config.settings import admin_settings


class AdminBase(BaseModel):
    first_name: str | None
    last_name: str
    email: EmailStr

    class Config:
        from_attributes = True

class AdminInfo(AdminBase):
    photo_url: str | None = None
    bio: str | None = None
    experience: str | None = None



class AdminLogIn(BaseModel):
    email: EmailStr

    class Config:
        from_attributes = True


class AdminAuth(AdminBase):
    password_hash: str

    class Config:
        from_attributes = True

    @model_validator(mode="after")
    def validate_admin(self) -> Self:
        if self.email != admin_settings.admin_email \
            or self.password_hash != admin_settings.admin_password:
            raise ValueError("Not correct data for Admin")
        return self

