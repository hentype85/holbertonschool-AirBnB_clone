#!/usr/bin/python3
"""tests"""

import pep8
import unittest
from models import storage
import datetime
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


class Test_Base_Model(unittest.TestCase):
    """tests base model"""

    def test_instance(self):
        new = BaseModel()
        self.assertIsInstance(new, BaseModel)
        self.assertEqual(issubclass(new.__class__, BaseModel), True)
        self.assertIs(type(new), BaseModel)
        self.assertEqual(type(new.id), str)

    def test_init_with_no_arguments(self):
        new = BaseModel()
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime.date)
        self.assertIsInstance(new.updated_at, datetime.date)
        self.assertEqual(type(new.created_at), type(new.updated_at))

    def test_str_representation(self):
        new = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(new.id, new.__dict__)
        self.assertEqual(str(new), expected_str)

    def test_save_updates_updated_at(self):
        new = BaseModel()
        old_updated_at = new.updated_at
        new.save()
        self.assertNotEqual(old_updated_at, new.updated_at)

    def test_to_dict_returns_dict_representation(self):
        new = BaseModel()
        new_dict = new.to_dict()
        self.assertIsInstance(new_dict, dict)
        self.assertEqual(new_dict["__class__"], "BaseModel")
        self.assertEqual(new_dict["id"], new.id)
        self.assertEqual(new_dict["created_at"], str(new.created_at))
        self.assertEqual(new_dict["updated_at"], str(new.updated_at))

    def test_to_dict_includes_additional_attributes(self):
        new = BaseModel()
        new.custom_attr = "custom_value"
        new_dict = new.to_dict()
        self.assertEqual(new_dict["custom_attr"], "custom_value")


if __name__ == "__main__":
    unittest.main()
