#!/usr/bin/python3
def safe_print_integer(value):
    """
    a function that prints an integer onl
    """
    try:
        print("{:d}".format(value))
        return True
    except(ValueError, TypeError):
        return False
