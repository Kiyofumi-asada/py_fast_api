from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models.user as userModel
from res_schemas.user import User

router = APIRouter()

# /user
# read
@router.get('/', response_model=List[User])
async def read_users(db: Session = Depends(get_db)):
    data = userModel.read_users(db=db)
    print("controller---------------",data)
    return data