#!/usr/bin/python3
"""
Module have a function that check if the object is an instance of a class
that inherited from
"""


def is_kind_of_class(obj, a_class):
    """a function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.
    """
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
