#!/usr/bin/python3
"""
The module have one function that divides all elements of a matrix.

"""


def matrix_divided(matrix, div):
    """a function that divides all elements of a matrix.

    Args:
        matrix (list): list of lists of integers or floats
        div: the number that all element divide by it

    Raises:
        TypeError: if element in matrix is not int or float
            rows in matrix not having the same size
            div in not int or float
        ZeroDivisionError: if div is 0

    Returns:
        new matrix
    """
    new_matrix = []
    # new_list = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        new_list = []
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists)\
                    of integers/floats")

        if len(row) == len(matrix[0]):
            pass
        else:
            raise TypeError("Each row of the matrix must have the same size")

        for elem in range(len(row)):
            if (type(row[elem]) not in [int, float]):
                raise TypeError("matrix must be a matrix (list of lists)\
                        of integers/floats")
            new_list.append(round(((row[elem]) / div), 2))
        new_matrix.append(new_list)

    return new_matrix
