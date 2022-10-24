from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from response_models.user import User
import models.user as userModel

router = APIRouter()

# /user
# read
@router.get('/', response_model=List[User])
async def read_users(db: Session = Depends(get_db)):
    data = userModel.read_users(db=db)
    return data