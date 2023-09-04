#!/usr/bin/python3
"""
define a function that all elements of a meyrix
takes two arguments
Args: a matrix and divider
"""


def matrix_divided(matrix, div):
    """
    implimenting the function
    """
    new_matrix = []
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    length = len(matrix)
    for i in range(length):
        if not isinstance(matrix[i], list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if i > 0:
            if len(matrix[i]) != len(matrix[i - 1]):
                raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if (not isinstance(matrix[i][j], int)) and (not isinstance(matrix[i][j], float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

        if div == 0:
            raise ZeroDivisionError("division by zero")
        if (not isinstance(div, int)) and (not isinstance(div, float)):
            raise TypeError("div must be a number")

        my_list = list(map(lambda x: x / div, matrix[i]))
        my_list = ["{:.2f}".format(x) for x in my_list]
        new_list = []
        for i in my_list:
            new_list.append(float(i))
        new_matrix.append(new_list)
    return list(new_matrix)
