#!/usr/bin/python3
""" Unittest for places.py file """
import unittest
import pep8
from api.v1.views import places
import inspect


class TestPlaces(unittest.TestCase):
    """ Class for Test places module """
    all_functions = inspect.getmembers(places, inspect.isfunction)
    def test_file_doc(self):
        """ Test file places Doc """
        self.assertIsNotNone(places.__doc__)

    def test_functions_doc(self):
        """ test functions Docs """
        all_functions = TestPlaces.all_functions
        for func in all_functions:
            self.assertisNotNone(func[1].__doc__)

    def test_pep8(self):
        """ Test pep8 style """
        style = pep8.StyleGuide(quite=True)
        f = style.check_files(['api/v1/views/places.py'])
        self.assertEqual(f.total_errors, 0, "Fix pep8")

if __name__ == "__main__":
    unittest.main()
