#!/usr/bin/python3
"""class FileStorage"""

import json


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
            fd.write(json.dumps(dictionary))      

    def reload(self):
        """deserializes the JSON file to __objects"""
