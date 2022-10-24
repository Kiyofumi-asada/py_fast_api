from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from response_models.user import User
import models.task as taskModel

router = APIRouter()

# /task
# read
@router.get('/', response_model=List[User])
async def read_task_list(db: Session = Depends(get_db)):
    return taskModel.read(db=db)