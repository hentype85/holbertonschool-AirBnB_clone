#!/usr/bin/python3
"""
Unittest for State class
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """ Tests for State Class"""

    def setUp(self):
        """Set up test data"""
        self.state = State()

    def test_name_attribute(self):
        """Test the name attribute"""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "")

    def test_name_assignment(self):
        """Test assigning a value to the name attribute"""
        self.state.name = "Salinas"
        self.assertEqual(self.state.name, "Salinas")

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_str_method(self):
        """Test the __str__ method"""
        expected_str = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)

    def test_save_method(self):
        """Test the save method"""
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(self.state.updated_at, old_updated_at)

if __name__ == "__main__":
    unittest.main()