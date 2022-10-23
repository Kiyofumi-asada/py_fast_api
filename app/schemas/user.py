from database import Base
from sqlalchemy import Column, String, Boolean ,Integer
from sqlalchemy.orm import relationship
from .mixins import TimestampMixin

class User(Base, TimestampMixin):
    __tablename__ = 'user'
    id=Column(Integer,primary_key=True, autoincrement=True)
    userName = Column(String(255), nullable=False)
    isDelete = Column(Boolean(), default=False)

    # relation
    task = relationship(
        'Task',
        back_populates='user'
    )