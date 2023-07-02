#!/usr/bin/python3

def add_integer(a, b=98):
    """Function that add two integers

    Args:
        a (int): First integer argument to add
        b (int): second integer argument to add

    Raises:
        TypeError: if type of a or b not integers or floats
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
