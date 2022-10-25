from sqlalchemy.orm import Session
from schemas.user import User

# get
def read(db: Session):
    data = db.query(User).all()
    return data

# post

# put

# delete