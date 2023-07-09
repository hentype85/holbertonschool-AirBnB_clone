#!/usr/bin/python3
"""
Unittest for User class
"""
import pep8
import unittest
from models.user import User
from models.base_model import BaseModel


class TestCodeFormat(unittest.TestCase):
    """ Test pep8"""

    def test_pep8_conformance(self):
        """ Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../models/user.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")

    def test_pep8_conformance_test(self):
        """ Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../tests/test_models/test_user.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")


class TestUser(unittest.TestCase):
    """ Tests for User Class"""

    def test_user_class(self):
        """ Tests if the user class exist and have attributes"""
        first_user = User()
        self.assertIsInstance(first_user, User)
        self.assertTrue(hasattr(first_user, "email"))
        self.assertAlmostEqual(first_user.email, "")
        self.assertTrue(hasattr(first_user, "password"))
        self.assertAlmostEqual(first_user.password, "")
        self.assertTrue(hasattr(first_user, "first_name"))
        self.assertAlmostEqual(first_user.first_name, "")
        self.assertTrue(hasattr(first_user, "last_name"))
        self.assertAlmostEqual(first_user.last_name, "")

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertTrue(issubclass(User, BaseModel))


if __name__ == "__main__":
    unittest.main()
