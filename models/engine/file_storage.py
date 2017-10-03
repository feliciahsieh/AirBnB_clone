#!/usr/bin/python3
"""class Filestorage"""
import json


class FileStorage:
    """class FileStorage"""
    def __init__(self):
        """
        __init__ - constructor method for class FileStorage
        Args:
            None
        Return:
            None
        """
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """
        all - returns the dictionary __objects
        Args:
            None
        Return:
            None
        """
        return self.__objects

    def new(self, obj):
        """
        new - sets in __objects the obj given
        Args:
            obj(unk) - object to copy into __objects dictionary
        Return:
            None
        """
        self.__objects[obj.__class__.__name__ + "." + str(obj.id)] = obj

    def save(self):
        """
        save - serializes __objects to JSON file
        Args:
            None
        Return:
            None
        """
        js = {}
        for k in self.__objects:
            js[k] = self.__objects[k].to_dict()
        js = json.dumps(js)
        with open(self.__file_path, "w") as jsf:
            jsf.write(js)

    def reload(self):
        """
        reload - deserializes JSON file back to __objects
        Arg:
            None
        Return:
            None
        """
        from models.base_model import BaseModel
        from models.user import User
        classesD = {'BaseModel': BaseModel, 'User': User}
        try:
            with open(self.__file_path, "r") as jsf:
                js = jsf.read()
            js = json.loads(js)
            for key in js:
                name = key.split(".")[0]
                if name in classesD:
                    self.__objects[key] = classesD[name](**js[key])
        except:
            return
