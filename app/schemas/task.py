from database import Base
from sqlalchemy import Column, ForeignKey, String, Boolean, Integer
from sqlalchemy.orm import relationship
from .mixins import TimestampMixin


class Task(Base, TimestampMixin):
    __tablename__ = 'task'

    id=Column(Integer,primary_key=True, autoincrement=True)
    title = Column(String(256), nullable=False)
    selectedOptionId = Column(Integer,default=-1, nullable=False)
    workContents = Column(String(256), nullable=True)
    selectedOptionId = Column(Integer, nullable=True)
    manDay = Column(Integer, nullable=True)
    requester = Column(String(256), nullable=True)
    progress = Column(Integer, nullable=True)
    note = Column(String(256), nullable=True)
    isDelete = Column(Boolean(), default=False)

    # relation
    userId = Column(
        ForeignKey('user.id'),
        nullable=True
    )
    user = relationship(
        'User',
        back_populates='task'
    )