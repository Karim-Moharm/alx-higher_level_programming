#!/bin/usr/python3
"""Module for rectangle sub-class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """init magic method that works as a constructor
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
