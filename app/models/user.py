from sqlalchemy.orm import Session
from ajax_models.user import PostReqUserModel, PutReqUserModel
from schemas.user import User as UserSchema

# get

# post
def create(body: PostReqUserModel, db: Session):
    user = UserSchema(userName = body.userName)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

# put
def update(body: PutReqUserModel, db: Session):
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
