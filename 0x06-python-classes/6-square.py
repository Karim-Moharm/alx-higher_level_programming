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

    @property
    def size(self):
        """Call the function to check property

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        if type(vlaue) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        pass

    def area(self):
        """Method to Calculate the area of the square

        Returns:
            The area of the square
        """
        return self.__size ** 2
