#!/usr/bin/python3
""" Test File for DBStorage class """
import models
import pep8
from os import getenv
import unittest
import MySQLdb
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.engine.base import Engine


class TestDBStorage(unittest.TestCase):
    """ TestDBStorage Class to test db_fileStorage engine"""
    @classmethod
    def setUpClass(cls):
        """ setUpClass fucntion """
        if type(models.storage) == DBStorage:
            cls.storage = DBStorage()
            Base.metadata.create_all(cls.storage._DBStorage__engine)
            Session = sessionmaker(bind=cls.storage._DBStorage__engine)
            cls.storage._DBStorage__session = Session()
            cls.user = User(email="jmaes@alxswe.com", password="james123")
            cls.storage._DBStorage__session.add(cls.user)
            cls.state = State(name="California")
            cls.storage._DBStorage__session.add(cls.state)
            cls.city = City(name="NYC", state_id=cls.state.id)
            cls.storage._DBStorage__session.add(cls.city)
            cls.place = Place(city_id=cls.city.id,
                              user_id=cls.user.id, name="Washinton",
                              number_rooms=3, number_bathrooms=2, max_guest=12,
                              price_by_night=200)
            cls.storage._DBStorage__session.add(cls.place)
            cls.amenity = Amenity(name="Wifi")
            cls.storage._DBStorage__session.add(cls.amenity)
            cls.review = Review(text="Reviews", place_id=cls.place.id,
                                user_id=cls.user.id)
            cls.storage._DBStorage__session.add(cls.review)
            cls.storage._DBStorage__session.commit()

    @classmethod
    def tearDownClass(cls):
        """ tearDownClass fucntion """
        if type(models.storage) == DBStorage:
            cls.storage._DBStorage__session.delete(cls.state)
            cls.storage._DBStorage__session.delete(cls.city)
            cls.storage._DBStorage__session.delete(cls.amenity)
            cls.storage._DBStorage__session.delete(cls.user)
            cls.storage._DBStorage__session.delete(cls.review)
            cls.storage._DBStorage__session.delete(cls.place)
            cls.storage._DBStorage__session.commit()

            del cls.state
            del cls.city
            del cls.amenity
            del cls.user
            del cls.review
            del cls.place
            del cls.storage

    def test_pep8(self):
        """ test pep8 style """
        style = pep8.StyleGuide(quit=True)
        f = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(f.total_errors, 0, "fix pep8")

    def test_docstring(self):
        """ Check for docstring """
        self.assertIsNotNone(DBStorage.__doc__)
        self.assertIsNotNone(DBStorage.__init__.__doc__)
        self.assertIsNotNone(DBStorage.all.__doc__)
        self.assertIsNotNone(DBStorage.delete.__doc__)
        self.assertIsNotNone(DBStorage.new.__doc__)
        self.assertIsNotNone(DBStorage.reload.__doc__)
        self.assertIsNotNone(DBStorage.save.__doc__)

    def test_attributes(self):
        """ Check Attributes """
        self.assertTrue(isinstance(self.storage._DBStorage__session, Session))
        self.assertTrue(isinstance(self.storage._DBStorage__engine, Engine))

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Test Engine FileStorage")
    def test_methods(self):
        """ Check Methods """
        self.assertTrue(hasattr(DBStorage, "__init__"))
        self.assertTrue(hasattr(DBStorage, "all"))
        self.assertTrue(hasattr(DBStorage, "delete"))
        self.assertTrue(hasattr(DBStorage, "new"))
        self.assertTrue(hasattr(DBStorage, "reload"))
        self.assertTrue(hasattr(DBStorage, "save"))

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Test Engine FileStorage")
    def test_all(self):
        """ Test all() method """
        objs = self.storage.all()
        self.assertEqual(type(objs), dict)
        self.assertEqual(len(objs), 6)

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Test Engine FileStorage")
    def test_all_cls(self):
        """ Test all(cls) method """
        state = self.storage.all(State)
        self.assertEqual(type(state), dict)
        self.assertEqual(len(state), 1)
        self.assertEqual(self.state, list(state.values())[0])

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Test Engine FileStorage")
    def test_new(self):
        """ Test new() method """
        state = State(name="California")
        self.storage.new(state)
        st = list(self.storage._DBStorage__session.new)
        self.assertIn(state, st)

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Test Engine FileStorage")
    def test_save(self):
        """ Test save() method """
        state = State(name="Gorgia")
        self.storage._DBStorage__session.add(state)
        self.storage.save()
        username = getenv("HBNB_MYSQL_USER")
        password = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        con = MySQLdb.connect(user=username, passwd=password, db=db)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM states WHERE name = 'Gorgia'")
        query = cursor.fetchall()
        self.assertEqual(len(query), 1)
        self.assertEqual(state.id, query[0][0])

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Test Engine FileStorage")
    def test_delete(self):
        """ Test delete() method """
        state = State(name="Gorgia")
        self.storage._DBStorage__session.add(state)
        self.storage._DBStorage__session.commit()
        self.storage.delete(state)
        self.assertIn(state, list(self.storage._DBStorage__session.deleted))

    @unittest.skipIf(type(models.storage) == FileStorage,
                     "Test Engine FileStorage")
    def test_reload(self):
        """ Test reload() method """
        curr_session = self.storage._DBStorage__session
        self.storage.reload()
        self.assertIsInstance(self.storage._DBStorage__session, Session)
        self.assertNotEqual(self.storage._DBStorage__session, curr_session)
        self.storage.__DBStorage__session = curr_session


if __name__ == "__main__":
    unittest.main()
