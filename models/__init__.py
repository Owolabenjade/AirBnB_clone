#!/usr/bin/python3
"""
__init__.py script to initialize the models package
"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
