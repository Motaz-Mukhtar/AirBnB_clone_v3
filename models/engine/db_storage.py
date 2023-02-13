#!/usr/bin/python3
""" DBStorage Class File """
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.state import State
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


class DBStorage:
    """ Define DBStorage class

        Attributes:
            __engine: linked to MySQL database
            __session: create the currnet database session
    """
    __engine = None
    __session = None

    def __init__(self):
        """ create the engine self.__engine and self.__session"""
        username = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(username, password, host, db),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ query on the currnet database session (self.__session)
            all objects depeding of the class name, if cls=None
            query all types of objects.
        """
        if cls is None:
            objects = self.__session.query(State).all()
            objects.extend(self.__session.query(City).all())
            objects.extend(self.__session.query(User).all())
            objects.extend(self.__session.query(Place).all())
            objects.extend(self.__session.query(Review).all())
            objects.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objects = self.__session.query(cls)
        return {"{}.{}".format(type(i).__name__, i.id): i for i in objects}

    def new(self, obj):
        """ add the object to the currnet database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the currnet database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete obj from the currnet database session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self,):
        """ create all talbes in the currnet database and new session """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """ call close() method on the private session attribute  """
        self.__session.close()
