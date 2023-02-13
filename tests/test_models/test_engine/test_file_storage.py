#!/usr/bin/python3
""" Test FileStorage Class"""
import unittest
import os
import json
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class Test_FileStorage(unittest.TestCase):
    """ Test FileStorage Class """
    @classmethod
    def setUpClass(cls):
        """ setUpClass function """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        cls.storage = FileStorage()
        cls.base = BaseModel()
        key = "{}.{}".format(type(cls.base).__name__, cls.base.id)
        cls.storage._FileStorage__objects[key] = cls.base
        cls.user = User()
        key = "{}.{}".format(type(cls.user).__name__, cls.user.id)
        cls.storage._FileStorage__objects[key] = cls.user
        cls.state = State()
        key = "{}.{}".format(type(cls.state).__name__, cls.state.id)
        cls.storage._FileStorage__objects[key] = cls.state
        cls.city = City()
        key = "{}.{}".format(type(cls.city).__name__, cls.city.id)
        cls.storage._FileStorage__objects[key] = cls.city
        cls.amenity = Amenity()
        key = "{}.{}".format(type(cls.amenity).__name__, cls.amenity.id)
        cls.storage._FileStorage__objects[key] = cls.amenity
        cls.place = Place()
        key = "{}.{}".format(type(cls.place).__name__, cls.place.id)
        cls.storage._FileStorage__objects[key] = cls.place
        cls.review = Review()
        key = "{}.{}".format(type(cls.review).__name__, cls.review.id)
        cls.storage._FileStorage__objects[key] = cls.review

    @classmethod
    def tearDownClass(cls):
        """ tearDownClass fucntion """
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.base
        del cls.city
        del cls.state
        del cls.amenity
        del cls.place
        del cls.user
        del cls.review

    def test_docstring(self):
        """ Check for docstring """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.__init__.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.delete.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)

    def test_attribute(self):
        """ Check Attributes """
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_methods(self):
        """ Check Methods """
        self.assertTrue(hasattr(FileStorage, "__init__"))
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "delete"))
        self.assertTrue(hasattr(FileStorage, "reload"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "new"))

    def test_init(self):
        """ Test type of storage """
        self.assertIsInstance(self.storage, FileStorage)

    def test_all(self):
        """ Test all() method """
        objs = self.storage.all()
        self.assertEqual(type(objs), dict)
        self.assertIs(objs, FileStorage._FileStorage__objects)
        self.assertEqual(len(objs), 7)

    def test_all_obj(self):
        """ Test all(obj) method """
        objs = self.storage.all(BaseModel)
        self.assertEqual(type(objs), dict)
        self.assertEqual(self.base, list(objs.values())[0])
        self.assertEqual(len(objs), 1)

    def test_new(self):
        """ Test new() method """
        model = BaseModel()
        self.storage.new(model)
        store = FileStorage._FileStorage__objects
        key = "{}.{}".format(type(model).__name__, model.id)
        self.assertIn(key, store.keys())
        self.assertIn(self.base, store.values())

    def test_save(self):
        """ Test save() method """
        self.storage.save()
        with open("file.json", mode='r', encoding="utf-8") as f:
            texts = f.read()
            self.assertIn("BaseModel." + self.base.id, texts)
            self.assertIn("User." + self.user.id, texts)
            self.assertIn("City." + self.city.id, texts)
            self.assertIn("State." + self.state.id, texts)
            self.assertIn("Place." + self.place.id, texts)
            self.assertIn("Amenity." + self.amenity.id, texts)
            self.assertIn("Review.", self.review.id, texts)

    def test_reload(self):
        """ Test reload() method """
        model = BaseModel()
        with open("file.json", mode='w', encoding="utf-8") as f:
            key = "{}.{}".format(type(model).__name__, model.id)
            json.dump({key: model.to_dict()}, f)
        self.storage.reload()
        store = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + model.id, store)

    def test_reload_no_file(self):
        try:
            self.storage.reload()
        except Exception:
            self.fail

    def test_delete(self):
        """ Test delete() method """
        model = BaseModel()
        key = "{}.{}".format(type(model).__name__, model.id)
        FileStorage._FileStorage__objects[key] = model
        self.storage.delete(model)
        self.assertNotIn("BaseModel." + model.id,
                         FileStorage._FileStorage__objects)

    def test_delete_nonexistant(self):
        try:
            self.storage.delete(State())
        except Exception:
            self.fail


if __name__ == "__main__":
    unittest.main()
