#!/usr/bin/python3
"""Test File for models/user.py file"""
import unittest
from datetime import datetime
from models.user import User

class TestUser(unittest.TestCase):
    """Test Class for User"""

    def test_id(self):
        """Test the User.id"""
        base1 = User()
        self.assertEqual(type(base1.id), str)

    def test_date(self):
        """Test the created_at and update_at attributes"""
        base1 = User()
        self.assertEqual(type(base1.created_at), datetime)
        self.assertEqual(type(base1.updated_at), datetime)
        self.assertEqual(base1.created_at, datetime.utcnow())

    def test_attributes(self):
        """Check Exist Attributes"""
        user1 = User()
        self.assertTrue(hasattr(user1, 'email'))
        self.assertTrue(hasattr(user1, 'password '))
        self.assertTrue(hasattr(user1, 'first_name '))
        self.assertTrue(hasattr(user1, 'last_name '))

    def test_str(self):
        """Test the User.__str__()"""
        base1 = User()
        string = "[{}] ({}) {}".format(type(base1).__name__, base1.id, base1.__dict__)
        self.assertEqual(base1.__str__(), string)

    def test_save(self):
        """Test the User.save()"""
        base1 = User()
        base1.save()
        update = datetime.utcnow()
        self.assertEqual(type(base1.updated_at), type(update))

    def test_to_dict(self):
        """Test the User.to_dict()"""
        base1 = User()
        my_dict = base1.__dict__.copy()
        my_dict['__class__'] = str(type(base1).__name__)
        my_dict['created_at'] = base1.created_at.isoformat()
        my_dict['updated_at'] = base1.updated_at.isoformat()
        self.assertEqual(base1.to_dict(), my_dict)
        self.assertDictEqual(base1.to_dict(), my_dict)

    def test_docstring(self):
        """Test the docstring"""
        base1 = User()
        self.assertIsNotNone(base1.__doc__)
        self.assertIsNotNone(base1.__init__.__doc__)
        self.assertIsNotNone(base1.save.__doc__)
        self.assertIsNotNone(base1.to_dict.__doc__)
        self.assertIsNotNone(base1.__str__.__doc__)


if __name__ == '__main__':
    unittest.main()
