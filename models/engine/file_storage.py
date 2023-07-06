#!/usr/bin/python3
"""class FileStorage"""
import json
import os
from models.base_model import BaseModel


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
        k = obj.__class__.__name__ + "." + obj.id
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
        try:
            with open(self.__file_path, "r") as fd:
                for k, v in (json.load(fd)).items():
                    self.__objects[k] = eval(v["__class__"])(**v)
        except FileNotFoundError:
            pass
