#!/usr/bin/ptyhon3
"""The square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """The init magic mehtod
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """str method for class Rectangle
        """
        return "[{}] ({}) {}/{} - {}".format(
                self.__class__.__name__,
                self.id,
                self.x, self.y,
                self.size)

    @property
    def size(self):
        """property method for size of the square
        Returns:
            size of square
        """
        return self.width

    @size.setter
    def size(self, value):
        """setter method for size attr of the square
        """
        if type(value) != int:
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
