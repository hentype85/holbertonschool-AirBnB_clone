#!/usr/bin/python3
"""Son todos los test que se me ocurrieron para probar el base model
"""
import unittest
from models.base_model import BaseModel


class Test_Base_Model(unittest.TestCase):
    """Son todos los test que se me ocurrieron para probar el base model
    """

    def create_class(self):
        """create class
        """
        self.my_model = BaseModel()
        self.assertTrue(hasattr(self.my_model, 'id'))
        self.assertTrue(hasattr(self.my_model, 'created_at'))
        self.assertTrue(hasattr(self.my_model, 'updated_at'))

    def test_set_name(self):
        """test set name
        """
        self.my_model.name = "My First Model"
        self.assertAlmostEqual(self.my_model.name, "My First Model")

    def test_set_number(self):
        """test set number
        """
        self.my_model.my_number = 89
        self.assertAlmostEqual(self.my_model.my_number, 89)

    def test_types(self):
        """test types
        """
        self.assertIsInstance(self.my_model.id, str)
        self.assertIsInstance(self.my_model.created_at, datetime)
        self.assertIsInstance(self.my_model.updated_at, datetime)
        self.assertIsInstance(self.my_model.to_dict(), dict)

    def test_to_dict(self):
        """test to dict
        """
        self.my_model_json = self.my_model.to_dict()
        self.assertIsInstance(self.my_model_json[created_at], str)
        self.assertIsInstance(self.my_model_json[updated_at], str)
        self.assertAlmostEqual(self.my_model_json[__class__], "BaseModel")

    def test_to_dict_2(self):
        """test to dict_2
        """
        self.assertIn('id', self.my_model.to_dict())
        self.assertIn('created_at', self.my_model.to_dict())
        self.assertIn('updated_at', self.my_model.to_dict())

    def test_save(self):
        """test save
        """
        old_updated_at = self.my_model.updated_at
        self.my_model.save()
        new_updated_at = self.my_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)


if __name__ == "__main__":
    unittest.main()
