#!/usr/bin/python3
"""class FileStorage"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """class that serializes instances to a JSON
    file and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets __objects the obj with key"""
        k = obj.__class__.__name__ + "." + obj.__dict__["id"]
        self.__objects[k] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        dictionary = {}
        for k, v in self.__objects.items():
            dictionary[k] = v.to_dict()
        with open(self.__file_path, "w") as fd:
            json.dump(dictionary, fd)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if not os.path.exists(self.__file_path):
            return
        else:
            with open(self.__file_path, "r") as fd:
                for k, v in json.load(fd).items():
                    self.__objects[k] = eval(v["__class__"])(**v)
