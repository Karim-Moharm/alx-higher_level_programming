#!/usr/bin/python3
"""an empty class called Square"""


class Square:
    """create a square.

    atributes:
    size (int): The size of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """The __init__ method for Square class

        Args:
            size: (int): instance size
            position: (tuple): instance position
        """
        self.size = size
        self.position = position

    def area(self):
        """Method to Calculate the area of the square

        Returns:
            The area of the square
        """
        return self.__size ** 2

    @property
    def size(self):
        """Call the function to check property

        Returns:
            The size of the square
        """
        return self.__size
