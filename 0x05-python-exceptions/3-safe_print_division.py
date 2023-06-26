#!/usr/bin/python3

def safe_print_division(a, b):
    """
    a function that divides 2 integers and prints the result.
    """
    try:
        print("Inside result: {}".format(a / b))
        return a / b
    except ZeroDivisionError:
        print("Inside result: {}".format(None))
