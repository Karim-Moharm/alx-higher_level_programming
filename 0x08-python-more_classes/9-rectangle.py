#!/usr/bin/python3
"""Module that define the rectangle class

"""


class Rectangle:
    """defines a rectangle by its area and Perimeter

    Attributes:
        width: width of the rectangel (private attr)
        height: height of the rectangel (private attr)
        number_of_instances: number of instances created (class atrr)
        print_symbol: Used as symbol for string representation (class attr)
    """
    number_of_instances = 0
    print_symbol = '#'

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
                char += str(self.print_symbol)
            if h < (self.__height - 1):
                char += '\n'
        return char

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the bigger area of two rectangles.

        Args:
            rect_1: The first rectangle (instance).
            rect_2: The second rectangle (instance).

        Raises:
            TypeError: If rect_1, rect_2 are not instances of Rectangle class.

        Returns:
            The rectangle with the larger area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns new Rectangle instance with equal dimentions.

        Args:
            cls: arg referes to class name
            size: size of width and height of the new instance

        Returns:
            new Rectangle instance with width = size = height
        """
        return cls(size, size)
