#!/usr/bin/python3
"""
Defines class User that inherits from BaseModel.
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    Defines the User class attributes.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

