#!/usr/bin/python3
"""class BaseModel"""
import uuid
import json
from datetime import datetime


class BaseModel():
    """BaseModel"""

    def __init__(self, *args, **kwargs):
        """initialize attributes"""
        strtimeFormat = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, strtimeFormat))
                elif k != '__class__':
                    setattr(self, k, v)
                else:
                    self.__class__.__name__ = v
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

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

    def to_dict(self):
        """Cambia el tipo de created_at y updated_at a un tipo serializado

        Returns:
            dict: Return the modified __dict__
        """
        new_dict = self.__dict__
        new_dict.update({'__class__': self.__class__.__name__})
        new_dict.update({'updated_at': self.updated_at.isoformat()})
        new_dict.update({'created_at': self.created_at.isoformat()})
        filename = "file.json"
        with open(filename, 'w') as file:
            file.write(json.dumps(new_dict))
        return new_dict
