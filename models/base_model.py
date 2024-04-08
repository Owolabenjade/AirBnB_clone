#!/usr/bin/python3
"""
Defines a class BaseModel that serves as the base class for all models in
the Airbnb clone project.
"""
import uuid
from datetime import datetime

class BaseModel:
    """
    Base class that defines all common attributes/methods for other classes.
    """
    
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance. Assigns unique ID and sets created_at
        and updated_at attributes to the current datetime.
        """
        if kwargs:
            # Handles deserialization from a dictionary
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            # Initialization for new instance creation
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def save(self):
        """Updates the updated_at attribute to the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance."""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy

    def __str__(self):
        """Returns a string representation of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

