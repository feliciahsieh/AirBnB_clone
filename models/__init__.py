#!/usr/bin/python3
"""init file"""
from models.engine.file_storage import FileStorage
__all__ = ["base_model", "user"]
storage = FileStorage()
storage.reload()
