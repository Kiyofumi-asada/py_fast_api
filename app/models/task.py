from sqlalchemy.orm import Session
from schemas.user import User

# get
def read(db: Session):
    data = db.query(User).all()
    return data

# TODO:taskapiを叩けるようにpost,put,delete
# post
def create(body, db: Session):
    user = UserSchema(userName = body.userName)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# put
def update(body, db: Session):
    user = db.query(UserSchema).filter(UserSchema.id == body.id)
    user.update({UserSchema.userName: request.userName})
    db.commit()
    return {"status": 200}

# delete
def logicalDelete(id: int, db: Session):
    user = db.query(UserSchema).filter(UserSchema.id == id)
    user.update({UserSchema.isDelete: True})
    db.commit()
    return {"status": 200}