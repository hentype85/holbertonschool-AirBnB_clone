#!/usr/bin/python3
"""class BaseModel"""

import uuid
from datetime import datetime


class BaseModel():
    """BaseModel"""

    def __init__(self, *args, **kwargs):
        """initialize attributes"""
        strtimeFormat = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, strtimeFormat))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """return string"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""
        new_dictionary = self.__dict__.copy()
        new_dictionary["__class__"] = self.__class__.__name__
        new_dictionary["created_at"] = self.created_at.isoformat()
        new_dictionary["updated_at"] = self.updated_at.isoformat()
        return new_dictionary
