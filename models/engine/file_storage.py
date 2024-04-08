#!/usr/bin/python3
"""
Defines the FileStorage class that serializes instances to a JSON
file and deserializes JSON file to instances.
"""
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        if obj:
            obj_id = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[obj_id] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {}
        for key in self.__objects:
            obj_dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for obj_id, obj_attrs in obj_dict.items():
                cls_name = obj_attrs["__class__"]
                if cls_name in globals():
                    self.__objects[obj_id] = globals()[cls_name](**obj_attrs)
        except FileNotFoundError:
            pass

