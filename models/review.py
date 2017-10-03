#!/usr/bin/python3
"""class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class Review"""

    def __init__(self, *args, **kwargs):
        """class constructon"""
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(**kwargs)
