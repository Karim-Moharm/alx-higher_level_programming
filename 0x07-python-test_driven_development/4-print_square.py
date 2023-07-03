#!/usr/bin/python3
"""
This module has a function that prints a square using #

Author: Karim Moharm
"""


def print_square(size):
    """ prints a square with the character #

    Args:
        size (int): size of the square

    Raises:
        TypeError: if size not int and if size is float and less than 0
        ValueError: if size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for w in range(size):
        for h in range(size):
            print("#", end="")
        print()
