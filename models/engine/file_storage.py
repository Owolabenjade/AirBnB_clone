#!/usr/bin/python3
"""
FileStorage class serializes instances to a JSON file and
deserializes JSON file to instances.
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """A class that manages file storage for HBNB models."""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        if obj:
            key = f'{obj.__class__.__name__}.{obj.id}'
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {obj: self.__objects[obj].to_dict() for obj in self.__objects.keys()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
            for obj_id in objs:
                obj_data = objs[obj_id]
                self.__objects[obj_id] = globals()[obj_data['__class__']](**obj_data)
        except FileNotFoundError:
            pass

