#!/usr/bin/python3

"""square class"""


class Square:
    """create a square.

    Attributes:
    size: private instance.
    """

    def __init__(self, size=0):
        """the __init__ special method

        Args:
            self: referred to the attribute
            size (int): size of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square

        Returns:
            Area of the square
        """
        return self.__size ** 2
