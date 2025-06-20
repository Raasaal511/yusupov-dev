from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attributes = True

class TokenAdminData(BaseModel):
    admin_email: str

    class Config:
        from_attributes = True


class TokenUserData(BaseModel):
    user_email: str

    class Config:
        from_attributes: True