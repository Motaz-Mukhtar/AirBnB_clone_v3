#!/usr/bin/python3
""" State Class File """
from os import getenv
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ Define State Class

        __tablename__: states
        name: Column String(128) can't be null
        cities: relationship with City, if State object deleted, all
                linked City object must be deleted automatically,
                and the reference name is state
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def cities(self):
            """ Returns the list of City instances with state_id """
            cities_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
