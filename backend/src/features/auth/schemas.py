from pydantic import BaseModel, EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str

    class Config:
        from_attributes = True

class TokenData(BaseModel):
    id: int

    class Config:
        from_attributes = True

