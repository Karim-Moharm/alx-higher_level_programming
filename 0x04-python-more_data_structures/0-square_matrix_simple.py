#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:]
    for row in new_matrix:
        new_matrix = list((map(lambda elem: elem**2 , row)))
    return new_matrix
