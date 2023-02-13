#!/usr/bin/python3
""" City Class File """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ Define City Class

        __tablename__: cities
        name: Column string(128) and can't be null
        state_id: Column string(60) Foreignkey to
                         states.id and can't be null
        places: relationship with Place, if the City object
                is deleted, all linked Place objects must be
                automatically deleted, Also the reference name user
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"),
                      nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
