#!/usr/bin/python3
"""file_storage module"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place


class FileStorage():
    """Class that manages file operations"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """Creates a new dictionary for an instance"""
        n_obj = "{}.{}".format(
            obj.__class__.__name__,
            obj.id
        )
        FileStorage.__objects[n_obj] = obj

    def save(self):
        """Saves a dict to a file"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict = value.to_dict()
            new_dict[key] = obj_dict

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(new_dict))

    def reload(self):
        """Reloads the file and loads it to __objects"""
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                for key, value in json.loads(f.read()).items():
                    instance = eval(value["__class__"])(**value)
                    FileStorage.__objects[key] = instance
        except BaseException:
            return
