#!/usr/bin/python3
"""
Module have a class that inherits from list class
"""


class MyList(list):
    """MyList class that inherits from list"""

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)
        Args:
            self: referes to instance of the class
        """
        new_list = self[:]
        new_list.sort()
        print(new_list)
