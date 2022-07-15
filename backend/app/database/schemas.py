from typing import Union, Dict, List
from pydantic import BaseModel


class PageBase(BaseModel):
    title: str
    content: str 
    parameters: Dict

class PageCreate(PageBase):
    pass

class Page(PageBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool
    pages: List[Page] = []

    class Config:
        orm_mode = True
