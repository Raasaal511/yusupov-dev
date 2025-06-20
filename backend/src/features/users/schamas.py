from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str


class UserAuth(UserBase):
    password_hash: str

