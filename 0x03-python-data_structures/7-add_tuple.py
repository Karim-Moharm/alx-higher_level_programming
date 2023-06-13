#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if tuple_a[0] == None:
            list_a = list(tuple_a)
            list_a[0] = 0
            tuple_a = tuple(list_a)
        else:
            list_a = list(tuple_a)
            list_a[1] = 0
            tuple_a = tuple(list_a)

    if len(tuple_b) < 2:
        if tuple_b[0] == None:
            list_b = list(tuple_b)
            list_b[0] = 0
            tuple_b = tuple(list_b)
        else:
            list_b = list(tuple_b)
            list_b[1] = 0
            tuple_b = tuple(list_b)

    index_1 = tuple_a[0] + tuple_b[0]
    index_2 = tuple_a[1] + tuple_b[1]
    new_tuple = (index_1, index_2)
    return tuple(new_tuple)
