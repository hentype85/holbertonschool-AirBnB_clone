#!/usr/bin/python3
"""unit tests"""

import unittest
import pep8
from models.base_model import BaseModel


class TestCodeFormat(unittest.TestCase):
    """test pep8"""
    def test_pep8_conformance(self):
        """Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../models/base_model.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")

    def test_pep8_conformance_test(self):
        """Test that conform to PEP8"""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ["../../tests/test_models/test_base_model.py"])
        self.assertEqual(result.total_errors, 1,
                         "Found pep8 code style errors and warnings")


class Test_BaseModel(unittest.TestCase):
    "class tests_BaseModel"

    def test_new_instance_BaseModel(self):
        new = BaseModel()
        self.assertIsInstance(new, BaseModel)

    def test_attributes(self):
        new = BaseModel()
        self.assertEqual(type(new.id), str)

    def test_class(self):
        new = BaseModel()
        self.assertEqual(issubclass(new.__class__, BaseModel), True)


if __name__ == "__main__":
    unittest.main()
