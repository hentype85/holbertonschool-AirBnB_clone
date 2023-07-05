#!/usr/bin/python3
"""class BaseModel"""

import uuid
from datetime import datetime


class BaseModel():
    """BaseModel"""

    def __init__(self):
        """Es solo el init, cuando creo el objeto le creo una id unica con
        uuid.uuid1, luego le asigno tambien un valor para cundo se crea.
        El [10:] es para recortar la cantidad de caracteres, ya que
        datetime.now() me retorna la fecha y ademas los segundos exactos,
        por lo que recorto todo ese string, guardando solo lo que queremos.
        """
        self.id = str(uuid.uuid1())
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
        return new_dict
