#!/usr/bin/python3
"""
The module has one function that prints a name
"""


def say_my_name(first_name, last_name=""):
    """a function that prints a full name

    Args:
        first_name (str): first name to print
        last_name (str): last name to print (optional)

    Raises:
        TypeError: if the names are not string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
