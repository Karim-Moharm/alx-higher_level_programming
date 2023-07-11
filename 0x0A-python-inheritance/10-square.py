#!/usr/bin/python3
"""
sub-class Square Module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square sub-class
    """
    def __init__(self, size):
        """The __init__ special method

        Attributes:
            size (int): size of square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
