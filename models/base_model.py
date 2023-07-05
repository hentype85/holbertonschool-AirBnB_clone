#!/usr/bin/python3
"""BaseModel
"""
from datetime import datetime
import uuid


class BaseModel():
    """BaseModel
    """

    def __init__(self):
        """Es solo el init, cuando creo el objeto le creo una id unica con
        uuid.uuid1, luego le asigno tambien un valor para cundo se crea.
        El [10:] es para recortar la cantidad de caracteres, ya que
        datetime.now() me retorna la fecha y ademas los segundos exactos,
        por lo que recorto todo ese string, guardando solo lo que queremos.
        """
        self.id = str(uuid.uuid1())
        self.created_at = (datetime.now())[10:]
        self.updated_at = self.created_at

    def __str__(self):
        """Hago el str segun lo piden, lo unico que me llega a chocar es
        lo de BaseModel, pero solo en el caso de hacerlo padre o abuelo
        por si herda no de problemas.
        Returns:
            str: Lo que pide el ejercicio.git
        """
        return "[{}] ({}) <{}>".format(self.__name__, self.id, self.__dict__)

    def save(self):
        """Actualiza el valor de updated al valor actual del datetime
        """
        self.updated_at = str(datetime.now())[10:]

    def to_dict(self):
        self.update({'__class__': self.__class__})
        return self.__dict__
