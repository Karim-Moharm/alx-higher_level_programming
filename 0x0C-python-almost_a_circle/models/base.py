#!/usr/bin/python3
"""Base class module
"""


class Base:
    """
    The Base Class of the project
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """init special method that works as constructor
        """
        if id in not None:
            self.id = id
        else:
            __nb_objects += 1
            id = __nb_objects
