#!/usr/bin/python3
"""Test File for models/city.py file"""
from models.city import City
import unittest
from datetime import datetime


class TestCity(unittest.TestCase):
    """Test Class for City"""

    def test_id(self):
        """Test the City.id"""
        base1 = City()
        self.assertEqual(type(base1.id), str)
    
    def test_date(self):
        """Test the created_at and update_at attributes"""
        base1 = City()
        self.assertEqual(type(base1.created_at), datetime)
        self.assertEqual(type(base1.updated_at), datetime)
        self.assertEqual(base1.created_at, datetime.utcnow())

    def test_attributes(self):
        """Check Exist Attributes"""
        city1 = City()
        self.assertTrue(hasattr(city1, 'name'))
        self.assertTrue(hasattr(city1, 'state_id'))

    def test_str(self):
        """Test the City.__str__()"""
        base1 = City()
        string = "[{}] ({}) {}".format(type(base1).__name__, base1.id, base1.__dict__)
        self.assertEqual(base1.__str__(), string)

    def test_save(self):
        """Test the City.save()"""
        base1 = City()
        base1.save()
        update = datetime.utcnow()
        self.assertEqual(type(base1.updated_at), type(update))

    def test_to_dict(self):
        """Test the City.to_dict()"""
        base1 = City()
        my_dict = base1.__dict__.copy()
        my_dict['__class__'] = str(type(base1).__name__)
        my_dict['created_at'] = base1.created_at.isoformat()
        my_dict['updated_at'] = base1.updated_at.isoformat()
        self.assertEqual(base1.to_dict(), my_dict)
        self.assertDictEqual(base1.to_dict(), my_dict)
    
    def test_docstring(self):
        """Test the docstring"""
        base1 = City()
        self.assertIsNotNone(base1.__doc__)
        self.assertIsNotNone(base1.__init__.__doc__)
        self.assertIsNotNone(base1.save.__doc__)
        self.assertIsNotNone(base1.to_dict.__doc__)
        self.assertIsNotNone(base1.__str__.__doc__)

if __name__ == '__main__':
    unittest.main()