#!/usr/bin/python3
"""class City"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """City
    """
    state_id = ""
    name = ""
