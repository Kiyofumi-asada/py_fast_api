from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from ajax_models.user import PostReqUserModel, PutReqUserModel, ResUserModel
import models.user as userModel

# /user
router = APIRouter()

# post
@router.post('/', response_model=ResUserModel)
def create_user(body: PostReqUserModel, db: Session = Depends(get_db)):
    return userModel.create(request, db)

# put
@router.put('/')
def update_user(body: PutReqUserModel, db: Session = Depends(get_db)):
    return userModel.update(request, db)

# delete
@router.delete('/{id}')
def update_user(id: int, db: Session = Depends(get_db)):
    return userModel.logicalDelete(id, db)