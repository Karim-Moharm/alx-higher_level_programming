#!/usr/bin/python3
def safe_print_integer(value):
    """
    a function that prints an integer onl
    """
    try:
        if value is int:
            print("{:d}".format(value))
            return True
    except:
        return False

