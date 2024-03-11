#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all objects"""
        return self.__objects

    def new(self, obj):
        """method new"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """method save"""
        for key, valu in FileStorage.__objects.items():
            dictio = valu.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(dictio, f)

    def reload(self):
        """method reload"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objects_dict = json.load(f)
                for key, val in objects_dict.items():
                    FileStorage.__objects[key] = eval(val["__class__"])(**val)
        except FileNotFoundError:
            pass
