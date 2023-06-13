#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_lst = list()
    for i in my_list:
        if i % 2:
            new_lst.append(False)
        else:
            new_lst.append(True)
    return new_lst
