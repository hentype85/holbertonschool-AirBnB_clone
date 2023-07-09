#!/usr/bin/python3
"""
Unittest for Amenity class
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


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


if __name__ == "__main__":
    unittest.main()
