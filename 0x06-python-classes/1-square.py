#!/usr/bin/python3
"""square class"""


class Square:
    """a class Square that defines a square

    Attributes:
        size (int): size of the square
    """

    def __init__(self, size):
        """the __init__ special method

        Args:
            self: the instance of class
            size: size of square
        """
        self.__size = size
