#!/usr/bin/python3
"""
File: base_model.py
"""
import json



class BaseModel:
    """
    BaseModel definition for AirBnB clone project
    """
    def __init__(self, id=None):
        """
        __init__ - initialze BaseModel object
        Args:
            id(int) - initialize obj with ID or use autonumber ad ID
        Return:
            None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        #self.created_at = x
        #self.updated_at = x

    def __str__(self):
        """
        __str__ - print method for BaseModel
        Args:
            None
        Return:
            None
        """
        #print("[{}] ({}) {}".format(class, self.id, self.__dict__))
    def save(self):
        """
        save - updates public instance attribute, udpated_at, and timestamp
        Args:
            None
        Return:
            None
        """
        #

    def to_dict(self):
        """
        to_dict - returns dictionary with all key/value pairs of __dict__
        Args:
            None
        Return:
            entire dictionary of instance
        """
        #self.__class__ = ?BaseModel
        #self.created_at =
        #self.updated_at =
        #return self.__dict__
