# from fastapi import exception
# from starlette.status import error
from sqlalchemy.orm import Session
from schemas import User


def read(db: Session):
    data = db.query(User).all()
    return data
