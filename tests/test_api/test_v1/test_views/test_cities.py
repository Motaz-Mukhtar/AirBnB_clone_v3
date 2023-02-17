#!/usr/bin/python3
""" Unittest for cities.py file """
import unittest
import pep8
from api.v1.views import cities
import inspect


class TestCities(unittest.TestCase):
    """ Class for Testing cities module """
    all_functions = inspect.getmembers(cities, inspect.isfunction)
    def test_file_doc(self):
        """ Test file cities Doc """
        self.assertIsNotNone(cities.__doc__)

    def test_functions_doc(self):
        """ Test functions doc """
        all_functions = TestCities.all_functions
        for func in all_functions:
            self.assertIsNotNone(func[1].__doc__)

    def test_pep8(self):
        """ Test pep8 style """
        style = pep8.StyleGuide(quite=True)
        f = style.check_files(['api/v1/views/cities.py'])
        self.assertEqual(f.total_errors, 0, "Fix pep8")

if __name__ == "__main__":
    unittest.main()
