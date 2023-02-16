#!/usr/bin/python3
import unittest
import pep8
from api.v1.views import users
import inspect


class TestUsers(unittest.TestCase):
    """ Class for Test users module """
    all_functions = inspect.getmembers(users, inspect.isfunction)
    def test_file_doc(self):
        """ Test file users Doc """
        self.assertIsNotNone(users.__doc__)

    def test_functions_doc(self):
        """ Test Functions Docs """
        all_functions = TestUsers.all_functions
        for func in all_functions:
            self.assertIsNotNone(func[1].__doc__)

    def test_pep8(self):
        """ Test pep8 style """
        style = pep8.StyleGuide(quite=True)
        f = style.check_files(['api/v1/views/users.py'])
        self.assertEqual(f.total.errors, 0, "Fix pep8")

if __name__ == "__main__":
    unittest.main()
