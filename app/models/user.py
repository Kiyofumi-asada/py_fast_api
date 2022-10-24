from sqlalchemy.orm import Session
from ajax_models.user import RequestUserModel
from schemas.user import User as UserSchema

# create
def create(request: RequestUserModel, db: Session):
    createData = UserSchema(userName = request.userName)
    db.add(createData)
    db.commit()
    db.refresh(createData)
    return createData

# read


# update

# delete