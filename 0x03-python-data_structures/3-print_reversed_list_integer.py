#!/usr/bin/python
def print_reversed_list_integer(my_list=[]):
    # my_list.reverse()
    reversed_list = my_list[::-1]
    for i in reversed_list:
        print("{:d}".format(i))
