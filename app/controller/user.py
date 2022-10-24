from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from ajax_models.user import RequestUserModel
import models.user as userModel

# /user
router = APIRouter()

# create
@router.post('/')
def create_user(request: RequestUserModel, db: Session = Depends(get_db)):
    return userModel.create(request, db)

# read

# update

# delete