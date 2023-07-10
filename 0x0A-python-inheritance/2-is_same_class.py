#!/usr/bin/python3
"""
Module have a function that check if the instance is object of a class
"""


def is_same_class(obj, a_class):
    """a function that returns True if the object is exactly an instance
       of the specified class ; otherwise False
    """
    return True if type(obj) == a_class else False
