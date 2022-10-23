from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models.user as userModel

from return_types.user import \
    User as UserSchema

router = APIRouter()

# read
@router.get('/', response_model=List[UserSchema])
async def read_users(db: Session = Depends(get_db)):
    data = userModel.read_users(db=db)
    print("--------------data",data)
    return data