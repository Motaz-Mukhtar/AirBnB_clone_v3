#!/usr/bin/python3
""" Place Class File """
import models
from os import getenv
from models.base_model import BaseModel
from models.base_model import Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ Define Place Class

        __tablename__: places
        city_id: Column String(60) ForeignKey to cities.id can't be null
        user_id: Column String(60) ForeignKey to users.id can't be null
        name: Column String(128) can't be null
        description: Column String(1024)
        number_rooms: Column Integer can't be null and 0 by default
        number_bathrooms: Column Integer can't be null and 0 by default
        max_guest: Column Integer can't be null 0 by default
        price_by_night: Column Integer can't be null 0 by default
        latitude: Column Float
        longitude: Column Float
        reviews: relationship with Review, if the Place object
                 is deleted all linked Review objects must be
                 automatically deleted Also, the reference name is user
        amenities: relationship with Amenity but also as secondary to
                   place_amenity with option viewonly=False
    """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """Returns the list of Review with place_id"""
            review_list = []

            for review in list(models.storage.all(Review).values()):
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """ Returns the list of Amenity with amenity_ids """
            amenities_list = []
            for amenity in list(models.storage.all(Amenity).values()):
                if amenity.id == self.id:
                    amenities_list.append(amenity)
            return amenities_list

        @amenities.setter
        def amenities(self, value):
            """
                amentities that handles append method for adding
                Amenity.id to the attribute amenity_ids, this
                method should accept only Amenity object.
            """
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
