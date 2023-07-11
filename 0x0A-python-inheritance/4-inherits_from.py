#!/usr/bin/python3
"""
Module having a function that checks if the object is an instance of a class
that inherited (directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """check if the objecy is instance of a class that inhereted from
    other class

    Args:
        obj: an object
        a_class: class

    Returns:
        True if the object instance of a class that inherited
        (directly or indirectly) from the specified class; otherwise False
    """
    return issubclass(type(obj), a_class) or isinstance(obj, a_class)
