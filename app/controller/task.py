from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from ajax_models.user import ResUserModel
import models.task as taskModel

# /task
router = APIRouter()

# get
@router.get('/', response_model=List[ResUserModel])
async def read_task_list(db: Session = Depends(get_db)):
    return taskModel.read(db=db)

# post


# put

# delete