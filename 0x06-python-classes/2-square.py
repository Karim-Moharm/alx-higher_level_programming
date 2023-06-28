#!/usr/bin/python3
"""square class"""


class Square:
    """a class Square that define a square

    Attributes:
        size: the size of the square
    """
    def __init__(self, size=0):
        """The __init__ special method

        Args:
            self: used as the instance of class
            size (int): size of the square (private attribute)

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
