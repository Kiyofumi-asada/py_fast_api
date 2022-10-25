from typing import List
from pydantic import BaseModel
from .task import Task

class PostReqUserModel(BaseModel):
  userName: str
class PutReqUserModel(BaseModel):
  id: int
  userName: str

class ResUserModel(BaseModel):
  id: int
  userName: str
  isDelete: bool
  # relation
  task: List[Task] = []
  class Config:
    orm_mode = True