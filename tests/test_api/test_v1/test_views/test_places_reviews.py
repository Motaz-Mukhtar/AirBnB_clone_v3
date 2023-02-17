#!/usr/bin/python3
""" Unittest for places_reviews.py file """
import unittest
import pep8
from api.v1.views import places_reviews
import inspect


class TestPlacesReviews(unittest.TestCase):
    """ Class for Testing places_reviews module """
    all_functions = inspect.getmembers(places_reviews, inspect.isfunction)
    def test_file_doc(self):
        """ Test file places_reviews Doc """
        self.assertIsNotNone(places_reviews.__doc__)

    def test_functions_doc(self):
        """ Test Functions Docs """
        all_functions = TestPlacesReviews.all_functions
        for func in all_functions:
            self.assertIsNotNone(func[1].__doc__)

    def test_pep8(self):
        """ Test pep8 style """
        style = pep8.StyleGuide(quite=True)
        f = style.check_files(['api/v1/views/places_reviews.py'])
        self.assertEqual(f.total_errors, 0, "Fix pep8")

if __name__ == "__main__":
    unittest.main()
