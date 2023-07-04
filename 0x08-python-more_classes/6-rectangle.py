#!/usr/bin/python3
"""Module that define the rectangle class

"""


class Rectangle:
    """defines a rectangle by its area and Perimeter

    Attributes:
        width: width of the rectangel (private attr)
        height: height of the rectangel (private attr)
        number_of_instances: number of instances created (class Attribute)
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        char = ""
        if self.__width == 0 or self.__height == 0:
            return char

        for h in range(self.__height):
            for w in range(self.__width):
                char += '#'
            if h < (self.__height - 1):
                char += '\n'
        return char

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

