#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
        [11, 2, 4],
        [78, 45, True]
    ]
print(matrix_divided(matrix, 3))
print(matrix)

print(matrix_divided(matrix2, 3))
print(matrix2)
