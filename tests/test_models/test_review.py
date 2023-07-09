#!/usr/bin/python3
"""
Unittest for Review class
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """ Tests for Review Class"""

    def test_review_attributes(self):
        """Test the attributes of the Review class"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_instance(self):
        """Test the instance of the Review class"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)


if __name__ == "__main__":
    unittest.main()
