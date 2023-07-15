#!/bin/usr/python3
"""Module for rectangle sub-class
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """init magic method that works as a constructor
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """property method for width
        Returns:
            value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for width attr
        Raises:
            TypeError: if the new width  value not int
            ValueError: if the new width value <= 0
        Args:
            value (int): new width value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """property method for height
        Returns:
            value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for height attr
        Raises:
            TypeError: if the new height value not int
            ValueError: if the new height value <= 0
        Args:
            value (int): new height value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """property method for x
        Returns:
            value of x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """setter method for x attr
        Raises:
            TypeError: if value of x not int
            ValueError: if new value < 0
        Args:
            value (int): new x value
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """property method for y
        Returns:
            value of y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """setter method for y attr
        Raises:
            TypeError: if value of y not int
            ValueError: if new value < 0
        Args:
            value (int): new y value
        """

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """return the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """print the rectangle with the char '#'
        """
        for y in range(self.y):
            print("")
        for h in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        """str method for class Rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self.x,
                self.y,
                self.width,
                self.height)
    
    def update(self, *args, **kwargs):
        """Updates rectangle class Method that 
        assign a value to each attribute

        Attr:
            *args (Non-Keyword Arguments): tuple 
            **kwargs (Keyword Arguments): dict
        """
        if len(args) != 0 and args is not None:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        
        elif len(kwargs) != 0 and kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
