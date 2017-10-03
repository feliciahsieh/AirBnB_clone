#!/usr/bin/python3
"""init file"""
from models.engine.file_storage import FileStorage
__all__ = ["base_model", "user", "state", "city", "amenity", "place", "review"]
storage = FileStorage()
storage.reload()
