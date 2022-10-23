from pydantic import BaseModel

class Task(BaseModel):
    id: int
    # TODO:returnData追加
    class Config:
        orm_mode = True