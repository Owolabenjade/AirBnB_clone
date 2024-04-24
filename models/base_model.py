#!/usr/bin/python3
"""
Defines a class BaseModel that serves as the base class for all models in
the AirBnB clone project.
"""
import uuid
from datetime import datetime

class BaseModel:
    """
    Base class that defines all common attributes/methods for other classes.
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
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def save(self):
        """
        Updates the instance's updated_at attribute to the current datetime
        and saves the instance to the file storage.
        """
        self.updated_at = datetime.now()
        from models import storage
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance.
        """
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

