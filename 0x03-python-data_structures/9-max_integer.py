#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    function that finds the biggest integer of a list
    """

    if not my_list:
        return None
    max_elm = my_list[0]
    for i in my_list:
        if i > max_elm:
            max_elm = i
    return max_elm
