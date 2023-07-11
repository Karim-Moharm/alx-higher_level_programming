#!/usr/bin/python3
"""
Rectangle class Module
"""

form 7-base_geometry import BaseGeometry
class Rectangle(BaseGeometry):
    """
    Rectangle subclass that inherit from BaseGeometry
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
