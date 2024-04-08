#!/usr/bin/python3
"""
Defines the BaseModel class for the AirBnB clone project.
"""
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    Defines all common attributes/methods for other classes in the AirBnB project.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()

    def save(self):
        """
        Updates the updated_at attribute to the current datetime.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance.
        """
        dict_copy = dict(self.__dict__)
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

