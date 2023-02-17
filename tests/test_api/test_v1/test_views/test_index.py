#!/usr/bin/python3
""" Unittest for index.py file """
import unittest
import pep8
from api.v1.views import index
import inspect


class TestIndex(unittest.TestCase):
    """ Class for Test index moudle """
    all_functions = inspect.getmembers(index, inspect.isfunction)
    def test_file_doc(self):
        """ Test file index Doc """
        self.assertIsNotNone(index.__doc__)

    def test_functions_doc(self):
        """ Test Functions Docs """
        all_functions = TestIndex.all_functions
        for func in all_functions:
            self.assertIsNotNone(func[1].__doc__)

    def test_pep8(self):
        """ Test pep8 style """
        style = pep8.StyleGuide(quite=True)
        f = style.check_files(['api/v1/views/index.py'])
        self.assertEqual(f.total_errors, 0, "Fix pep8")

if __name__ == "__main__":
    unittest.main()
