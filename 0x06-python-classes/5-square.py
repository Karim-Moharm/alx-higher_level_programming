#!/usr/bin/python3
"""The square class"""


class Square:
    """Square class that defines a square

    Attributes:
        size (int): private attribute
    """

    def __init__(self, size=0):
        """The __init__ special method

        Args:
            size (int): size of the square
        """
        self.size = size

    @property
    def size(self):
        """property method used as getter

        Returns:
            the size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """set the value of size and check for error

        Args:
            value (int): value  square size

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates the Area of square

        Returns:
            area of square
        """
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character"""
        if self.__size == 0:
            print()
        else:
            for h in range(self.__size):
                for w in range(self.__size):
                    print("#", end="")
                print()
