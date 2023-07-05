#!/usr/bin/python3
"""Module that creates a dynamic attribute
"""


class LockedClass:
    """class that creates only first_name attribute"""
    __slots__ = ('first_name', )
