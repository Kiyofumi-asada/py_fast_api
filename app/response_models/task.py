from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str
    selectedOptionId: int
    workContents: str
    selectedOptionId: int
    manDay: int
    requester: str
    progress: int
    note: str
    isDelete: bool

    class Config:
        orm_mode = True