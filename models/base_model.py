#!/usr/bin/python3
"""BaseModel Class"""
import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import DateTime

Base = declarative_base()


class BaseModel:
    """ Define BaseModel Class

      id Column: String(60) can't be null and it's primary key
      created_at Column: Datetime can't be null and the
                         default value is the current datetime
      updated_at Column: Datetime can't be null and the
                         default value is the currnet datetime
    """
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Initilize public instance attributes

            args(list): Empty list
            kwargs(dict): dictionary that
            contain key/value of the attirbutes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key == '__class__':
                    continue
                setattr(self, key, value)

    def save(self):
        """updates the public instance attribut
            update_at with the current datetime"""
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Returns dictionary containing
        all keys/values of the instance:"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = str(type(self).__name__)
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict.pop("_sa_instance_state", None)
        return my_dict

    def delete(self):
        """ delete the currnet instance from the storage """
        models.storage.delete(self)

    def __str__(self):
        """Return Representation of the
            Ojbect [<class name>] (<self.id>) <self.__dict__>"""
        c = self.__dict__.copy()
        c.pop("_sa_instance_state", None)
        return "[{}] ({}) {}".format(type(self).__name__, self.id, c)
