from typing import List
from pydantic import BaseModel
from typing import Optional


# user


class Pupil(BaseModel):
    id: int
    first_name: str
    second_name: str
    class_year: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: str
    first_name: str
    surname: str
    disabled: Optional[bool] = None


class UserCreate(UserBase):
    password: str


class User(BaseModel):
    id: int
    email: str
    hashed_password: str
    is_active: bool
    first_name: str
    surname: str

    # pupil: List[Pupil] = []

    class Config:
        orm_mode = True


class UserResponse(BaseModel):
    email: str
    first_name: str
    surname: str
    is_active: bool

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class UserInDB(User):
    pass
