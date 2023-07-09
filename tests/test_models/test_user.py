#!/usr/bin/python3
"""
Unittest for User class
"""
import unittest
from models.user import User


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


if __name__ == "__main__":
    unittest.main()
