from typing import List
from pydantic import BaseModel


# user


class Pupil(BaseModel):
    id: int
    first_name: str
    second_name: str
    class_year: str

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    first_name: str
    surname: str


class UserCreate(UserBase):
    password: str


class User(BaseModel):
    id: int
    email: str
    hashed_password: str
    is_active: bool

    # pupil: List[Pupil] = []

    class Config:
        orm_mode = True
