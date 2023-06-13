#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for rows in matrix:
        for elem in range(len(rows)):
            if elem == len(rows) - 1:
                print("{:d}".format(rows[elem]), end="")
            else:
                print("{:d}".format(rows[elem]), end=" ")
        print()
