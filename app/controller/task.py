from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from ajax_models.user import ResUserModel
import models.task as taskModel

# /task
router = APIRouter()

# TODO:taskapiを叩けるようにpost,put,delete
# get
@router.get('/', response_model=List[ResUserModel])
async def read_task_list(db: Session = Depends(get_db)):
    return taskModel.read(db=db)

# post
@router.post('/', response_model=ResUserModel)
def create_user(body, db: Session = Depends(get_db)):
    return taskModel.create(request, db)

# put
@router.put('/')
def update_user(body, db: Session = Depends(get_db)):
    return taskModel.update(request, db)

# delete
@router.delete('/{id}')
def update_user(id: int, db: Session = Depends(get_db)):
    return taskModel.logicalDelete(id, db)