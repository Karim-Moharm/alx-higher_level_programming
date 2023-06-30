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
        if type(value) is not int:
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
        if (type(value) is not tuple or
                value[0] < 0 or value[1] < 0 or
                value[0] is not int or value[1] is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Method to Calculate the area of the square

        Returns:
            The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for line in range(self.__position[1]):
                print()

            for h in range(self.__size):
                for space in range(self.__position[0]):
                    print("_", end="")
                for w in range(self.__size):
                    print("#", end="")
                print()
