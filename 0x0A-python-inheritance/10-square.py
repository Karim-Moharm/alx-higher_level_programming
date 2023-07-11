#!/usr/bin/python3
"""
sub-class Square Module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """The __init__ special method
        Args:
            size (int): size of square
        """
        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size
