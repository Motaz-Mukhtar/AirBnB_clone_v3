#!/usr/bin/python3
"""Test File for models/place.py file"""
from models.place import Place
import unittest
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Test Class for Place"""

    def test_id(self):
        """Test the Place.id"""
        base1 = Place()
        self.assertEqual(type(base1.id), str)
    
    def test_date(self):
        """Test the created_at and update_at attributes"""
        base1 = Place()
        self.assertEqual(type(base1.created_at), datetime)
        self.assertEqual(type(base1.updated_at), datetime)
        self.assertEqual(base1.created_at, datetime.utcnow())

    def test_attributes(self):
        """Check Exist Attributes"""
        place1 = Place()
        self.assertTrue(hasattr(place1, 'city_id'))
        self.assertTrue(hasattr(place1, 'user_id'))
        self.assertTrue(hasattr(place1, 'name'))
        self.assertTrue(hasattr(place1, 'description'))
        self.assertTrue(hasattr(place1, 'number_rooms'))
        self.assertTrue(hasattr(place1, 'number_bathrooms'))
        self.assertTrue(hasattr(place1, 'max_guest'))
        self.assertTrue(hasattr(place1, 'price_by_night'))
        self.assertTrue(hasattr(place1, 'latitude'))
        self.assertTrue(hasattr(place1, 'longitude'))
        self.assertTrue(hasattr(place1, 'amenity_ids'))

    def test_str(self):
        """Test the Place.__str__()"""
        base1 = Place()
        string = "[{}] ({}) {}".format(type(base1).__name__, base1.id, base1.__dict__)
        self.assertEqual(base1.__str__(), string)

    def test_save(self):
        """Test the Place.save()"""
        base1 = Place()
        base1.save()
        update = datetime.utcnow()
        self.assertEqual(type(base1.updated_at), type(update))

    def test_to_dict(self):
        """Test the Place.to_dict()"""
        base1 = Place()
        my_dict = base1.__dict__.copy()
        my_dict['__class__'] = str(type(base1).__name__)
        my_dict['created_at'] = base1.created_at.isoformat()
        my_dict['updated_at'] = base1.updated_at.isoformat()
        self.assertEqual(base1.to_dict(), my_dict)
        self.assertDictEqual(base1.to_dict(), my_dict)
    
    def test_docstring(self):
        """Test the docstring"""
        base1 = Place()
        self.assertIsNotNone(base1.__doc__)
        self.assertIsNotNone(base1.__init__.__doc__)
        self.assertIsNotNone(base1.save.__doc__)
        self.assertIsNotNone(base1.to_dict.__doc__)
        self.assertIsNotNone(base1.__str__.__doc__)

if __name__ == '__main__':
    unittest.main()