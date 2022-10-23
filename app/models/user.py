from sqlalchemy.orm import Session
from schemas.user import User

# read
def read_users(db: Session):
    data = db.query(User).all()
    print("models---------------------------",data)
    return data