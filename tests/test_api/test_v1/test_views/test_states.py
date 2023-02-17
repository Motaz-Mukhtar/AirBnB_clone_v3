#!/usr/bin/python3
""" Unittest for states.py file """
import unittest
import pep8
import inspect
from api.v1.views import states


class TestStates(unittest.TestCase):
    """ Class for Testing states module """
    all_functions = inspect.getmembers(states, inspect.isfunction)
    def test_file_doc(self):
        """ Test file Doc """
        self.assertIsNotNone(states.__doc__)

    def test_functions_doc(self):
        """ Test Functions doc """
        all_functions = TestStates.all_functions
        for func in all_functions:
            self.assertIsNotNonde(func[1].__doc__)

    def test_pep8(self):
        """ Test pep8 style """
        style = pep8.StyleGuide(quite=True)
        f = style.check_files(['api/v1/views/states.py'])
        self.assertEqual(f.total_errors, 0, "Fix pep8")

if __name__ == "__main__":
    unittest.main()
