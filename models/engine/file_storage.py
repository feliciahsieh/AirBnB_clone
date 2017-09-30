#!/usr/bin/python3
"""class Filestorage"""
import json


class FileStorage:
    """class FileStorage"""
    def __init__(self):
        """constructor method"""
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj given"""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """serializes __objects to Json File"""
        js = {}
        for k in self.__objects:
            js[k] = self.__objects[k].to_dict()
        js = json.dumps(js)
        with open(self.__file_path, "w") as jsf:
            jsf.write(js)

    def reload(self):
        """deserializes JSON file back to __objects"""
        try:
            with open(self.__file_path, "r") as jsf:
                js = jsf.read()
                #fix here
           self.__objects = json.loads(js)
        except:
            return
