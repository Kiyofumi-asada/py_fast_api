import controller.user as models
from database import get_db
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from types.user import User

router = APIRouter()

@router.get('/', response_model=List[User])
async def read(db: Session = Depends(get_db)):
    return models.read(db=db)
