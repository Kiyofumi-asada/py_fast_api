from typing import List
from pydantic import BaseModel
from .task import Task

class RequestUserModel(BaseModel):
  userName: str

class ResponseUserModel(BaseModel):
  id: int
  userName: str
  isDelete: bool
  # relation
  task: List[Task] = []
  class Config:
    orm_mode = True