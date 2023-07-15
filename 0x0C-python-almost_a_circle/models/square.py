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
        self.size= size

    def __str__(self):
        """str method for class Rectangle
        """
        return "[{}] ({}) {}/{} - {}".format(
                self.__class__.__name__,
                self.id,
                self.x, self.y,
                self.size) 
