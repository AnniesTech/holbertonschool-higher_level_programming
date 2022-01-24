#!/usr/bin/python3
""" This is 2-matrix_divided that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Returns the division of all elements of the matrix:
        matrix (list of list): first value
        div (int): int that will be the divider
        Return:
            the division of al elements of a matrix
    """

    if type(matrix) is not list:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    size = len(matrix[0])
    if size == 0:
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if len(row) is not size:
            raise TypeError("Each row of the matrix must have the same size")
        if type(row) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = [[round(b / div, 2) for b in i] for i in matrix]
    return new_matrix
