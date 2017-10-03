#!/usr/bin/python3                                                                                                                             
"""class Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """class Place"""
    def __init__(self, *args, **kwargs):
        """class constructor"""
        self.user_id = ""
        self.city_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitute = 0.0
        self.amenity_ids = []
        super().__init__(**kwargs)
