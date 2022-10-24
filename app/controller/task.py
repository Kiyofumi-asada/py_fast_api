from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from ajax_models.user import ResponseUserModel
import models.task as taskModel

# /task
router = APIRouter()

# create

# read
@router.get('/', response_model=List[ResponseUserModel])
async def read_task_list(db: Session = Depends(get_db)):
    return taskModel.read(db=db)

# update

# delete