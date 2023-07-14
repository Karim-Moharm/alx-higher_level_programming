#!/usr/bin/python3
"""Base class module
"""


class Base:
    """
    The Base Class of the project

    Attrs:
         __nb_objects: private class attribute
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """init special method that works as constructor
        Attrs:
            id (int): integer attribute for id
        """
        if id in not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
