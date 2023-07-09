#!/usr/bin/python3
"""
Unittest for State class
"""
import pep8
import unittest
from models.state import State
from models.base_model import BaseModel


class TestCodeFormat(unittest.TestCase):
    """ Test pep8"""

    def test_pep8_conformance(self):
        """ Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../models/state.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")

    def test_pep8_conformance_test(self):
        """ Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../tests/test_models/test_state.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")


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
        expected_str = "[State] ({}) {}".format(
            self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)

    def test_save_method(self):
        """Test the save method"""
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(self.state.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()
