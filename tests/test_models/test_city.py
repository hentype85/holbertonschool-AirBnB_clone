#!/usr/bin/python3
"""
Unittest for City class
"""
import pep8
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCodeFormat(unittest.TestCase):
    """ Test pep8"""

    def test_pep8_conformance(self):
        """ Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../models/city.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")

    def test_pep8_conformance_test(self):
        """ Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../tests/test_models/test_city.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")


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

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))


if __name__ == "__main__":
    unittest.main()
