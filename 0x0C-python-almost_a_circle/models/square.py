#!/usr/bin/python3
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

    def update(self, *args, **kwargs):
        """Updates square class Method that
        assign a value to each attribute

        Attr:
            *args (Non-Keyword Arguments): tuple
            **kwargs (Keyword Arguments): dict
        """
        if len(args) != 0 and args is not None:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]

        elif len(kwargs) != 0 and kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """return dict representation for the
        class Rectangle attributes
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
