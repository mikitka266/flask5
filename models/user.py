from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    id: int
    first_name: str
    last_name: str=None
    email: EmailStr = Field(max_length=128)
    password: str = Field(min_length=6)


class UserIn(BaseModel):
    first_name: str
    last_name: str=None
    email: EmailStr = Field(max_length=128)

    