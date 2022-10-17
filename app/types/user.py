from typing import List
from pydantic import BaseModel
from uuid import UUID
from .book import Book


class User(BaseModel):
    id: int
    userName: str
    isDelete: bool
    class Config:
        orm_mode = True