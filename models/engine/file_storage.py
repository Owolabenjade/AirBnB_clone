#!/usr/bin/python3
"""
Defines the FileStorage class that serializes instances to a JSON file
and deserializes JSON file to instances.
"""
import json
from models.base_model import BaseModel

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
            self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

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
            for obj in objs.values():
                cls_name = obj["__class__"]
                del obj["__class__"]
                if cls_name == "BaseModel":
                    self.__objects[obj['id']] = BaseModel(**obj)
        except FileNotFoundError:
            pass

