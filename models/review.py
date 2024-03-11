#!/usr/bin/python3
"""class method"""
from models.base_model import BaseModel


class Review(BaseModel):
    """review model"""
    place_id = ""
    user_id = ""
    text = ""
