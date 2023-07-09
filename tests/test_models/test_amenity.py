#!/usr/bin/python3
"""
Unittest for Amenity class
"""
import pep8
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestCodeFormat(unittest.TestCase):
    """ Test pep8"""

    def test_pep8_conformance(self):
        """ Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../models/amenity.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")

    def test_pep8_conformance_test(self):
        """ Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../tests/test_models/test_amenity.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")


class TestAmenity(unittest.TestCase):
    """Tests for Amenity Class"""

    def test_amenity_attributes(self):
        """Test the attributes of the Amenity class"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_instance(self):
        """Test the instance of the Amenity class"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))


if __name__ == "__main__":
    unittest.main()
