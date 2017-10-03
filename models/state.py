#!/usr/bin/python3
"""class state"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class State"""
    def __init__(self, *args, **kwargs):
        """class constructor"""
        self.name = ""
        super().__init__(**kwargs)
