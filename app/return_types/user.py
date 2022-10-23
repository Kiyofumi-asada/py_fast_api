from typing import List
from pydantic import BaseModel
from .task import Task


class User(BaseModel):
  id: int
  username: str
  isDelete: bool
  task: List[Task] = []
  class Config:
    orm_mode = True