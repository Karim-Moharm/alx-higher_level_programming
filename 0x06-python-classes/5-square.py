#!/usr/bin/python3
"""The square class"""


class Square:
    """Square class that defines a square

    Attributes:
        size (int): private attribute
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for h in range(self.__size):
                for w in range(self.__size):
                    print("#", end="")
                print()
