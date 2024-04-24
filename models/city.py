#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel

class City(BaseModel):
    """Represents a City with state_id and name."""
    state_id = ""
    name = "”

