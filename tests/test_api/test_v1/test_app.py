#!/usr/bin/python3
""" Unittest for app.py file """
import unittest
import pep8
from api.v1 import app
import inspect


class TestApp(unittest.TestCase):
    """ Class for Testing Flask app """
    all_functions = inspect.getmembers(app, inspect.isfunction)
    def test_file_doc(self):
        """ Test file app Doc """
        self.assertIsNotNone(app.__doc__)

    def test_functions_doc(self):
        """ Test Functions Docs """
        all_functions = TestApp.all_functions
        for func in all_functions:
            self.assertIsNotNone(func[1].__doc__)

    def test_pep8(self):
        """ Test pep8 style """
        style = pep8.StyleGuide(quite=True)
        f = style.check_files(['api/v1/app.py'])
        self.assertEqual(f.total_errors, 0, "Fix pepe8")

if __name__ == "__main__":
    unittest.main()

