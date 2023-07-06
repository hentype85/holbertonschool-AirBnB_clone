#!/usr/bin/python3
"""class BaseModel"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """BaseModel"""

    def __init__(self, *args, **kwargs):
        """initialize attributes"""
        strtimeFormat = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, strtimeFormat))
                if k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Hago el str segun el formato que piden.
        Returns:
            str: Lo que pide el ejercicio
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Actualiza el valor de updated al valor actual del datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Cambia el tipo de created_at y updated_at a un tipo serializado
        Returns:
            dict: Return the modified __dict__
        """
        new_dictionary = self.__dict__.copy()
        new_dictionary["__class__"] = self.__class__.__name__
        new_dictionary["created_at"] = self.created_at.isoformat()
        new_dictionary["updated_at"] = self.updated_at.isoformat()
        return new_dictionary
