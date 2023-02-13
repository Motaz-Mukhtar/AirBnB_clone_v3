#!/usr/bin/python3
""" User Class File """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ Define User Class

        __tablename__: users
        email: Column String(128) can't be null
        password: Column String(128) can't be null
        first_name: Column String(128) can be null
        last_name: Column String(128) can be null
        places: relationship with Place, if the User object
                deleted all linked Place object must be
                automatically delted, and the reference name is user
        reviews: relationship with Review, if the User object
                 deleted all linked Review object must be deleted
                 automatically, and the reference name is user
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")
