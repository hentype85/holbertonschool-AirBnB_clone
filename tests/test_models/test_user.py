#!/usr/bin/python3
"""User Class Tests"""

import unittest
import pep8
from models.user import User
from models.base_model import BaseModel


class TestCodeFormat(unittest.TestCase):
    """test pep8"""

    def test_pep8_conformance(self):
        """Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../models/user.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")

    def test_pep8_conformance_test(self):
        """Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../tests/test_models/test_user.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")


class Test_User(unittest.TestCase):
    """tests User"""

    def test_instance_user(self):
        new = User()
        self.assertIsInstance(new, User)
        self.assertEqual(issubclass(new.__class__, BaseModel), True)
        self.assertIs(type(new), User)
        self.assertEqual(type(new.id), str)


if __name__ == "__main__":
    unittest.main()
