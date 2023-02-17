#!/usr/bin/python3
""" Unittest for amenities.py file """
import unittest
import pep8
from api.v1.views import amenities
import inspect


class TestAmenities(unittest.TestCase):
    """ Class for Testing amenitites module """
    all_functions = inspect.getmembers(amenities, inspect.isfunction)
    def test_file_doc(self):
        """ Test amenities Doc """
        self.assertIsNotNone(amenities.__doc__)

    def test_functions(self):
        """ Test Functions Docs """
        all_functions = TestAmenities.all_functions
        for func in all_functions:
            self.assertIsNotNone(func[1].__doc__)

    def test_pep8(self):
        """ Test pep8 style """
        style = pep8.StyleGuide(quite=True)
        f = style.check_files(['api/v1/views/amenities.py'])
        self.assertEqual(f.total_errors, 0, "Fix pep8")

if __name__ == "__main__":
    unittest.main()
