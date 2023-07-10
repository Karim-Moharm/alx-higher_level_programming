#!/usr/bin/python3
"""
Module have a function that return a list of attributes and
method of an object
"""


def lookup(obj):
    """a function that returns the list of available attributes
    and methods of an object

    Args:
        obj: object

    Returns:
        a list object
    """

    return (dir(obj))
