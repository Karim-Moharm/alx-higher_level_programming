#!/usr/bin/python3
"""
Module having a function that adds a new attribute to an object
"""


def add_attribute(obj, name: str, value):
    if not hasattr(obj, obj.vars()):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
