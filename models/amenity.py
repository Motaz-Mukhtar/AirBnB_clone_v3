#!/usr/bin/python3
""" Amenity Class File """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Define Amenity Class

        __tablename__: amenities
        name: Column String(128) can't be null
        place_amenities: relationship to Place, also as
                         secondary to place_amenity with
                         option viewonly=False
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place",
                                   secondary="place_amenity",
                                   viewonly=False)
