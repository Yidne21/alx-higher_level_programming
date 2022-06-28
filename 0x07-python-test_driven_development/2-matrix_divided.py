#!/usr/bin/python3
"""Module which divides all elements of the given matrix with a given divisor"""
def matrix_divided(matrix, div):
    """Function which divides all elements of the given matrix with a given divisor and returnes the new matrix"""

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        list1 = []
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if (len(matrix[0]) != len(row)):
            raise TypeError("Each row of the matri must have the same size")
        for column in range(len(row)):
            if (type(row[column]) is not int) and (type(row[column]) is not float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            list1.append(round((row[column] / div), 2))
        new_matrix.append(list1)
    return new_matrix
