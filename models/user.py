#!/usr/bin/python3
"""class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """class User"""

    def __init__(self, *args, **kwargs):
        """class constructon"""
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(**kwargs)
