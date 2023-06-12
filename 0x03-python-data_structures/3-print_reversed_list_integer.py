#!/usr/bin/python
def print_reversed_list_integer(my_list=[]):
    if my_list:
       # reversed_list = my_list[::-1]
        #my_list.reverse()
        for i in my_list[::-1]:
            print("{:d}".format(i))
