#!/usr/bin/python3
"""
Unittest for City class
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Tests for City Class"""

    def test_city_attributes(self):
        """Test the attributes of the City class"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_instance(self):
        """Test the instance of the City class"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)


if __name__ == "__main__":
    unittest.main()
