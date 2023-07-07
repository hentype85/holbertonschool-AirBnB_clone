#!/usr/bin/python3
"""class Review"""
from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """Review
    """
    place_id = ""
    user_id = ""
    text = ""
