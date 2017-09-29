#!/usr/bin/python3
"""
File: base_model.py
"""
import uuid
import datetime


class BaseModel:
    """
    BaseModel definition for AirBnB clone project
    This is the core object from which all objects are derived
    """
    def __init__(self):
        """
        __init__ - initialze BaseModel object
        Args:
            id(int) - initialize obj with ID or use autonumber ad ID
        Return:
            None
        """
        self.id = str(uuid.uuid4())
        self.created_at = str(datetime.datetime.now())
        self.updated_at = self.created_at

    def __str__(self):
        """
        __str__ - print method for BaseModel
        Args:
            None
        Return:
            None
        """
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        save - updates public instance attribute, updated_at, with
        current timestamp
        Args:
            None
        Return:
            None
        """
        self.updated_at = str(datetime.datetime.now())

    def to_dict(self):
        """
        to_dict - returns dictionary with all key/value pairs of __dict__
        Args:
            None
        Return:
            entire dictionary of instance
        """
        return self.__dict__
