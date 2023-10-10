#!/usr/bin/python3
"""
divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    divides all matrix elements

    Args:
        matrix (list): a list of lists of integers or floats
        div (int): a number that the matrix is divided by
    """
    message = "matrix must be a matrix (list of lists) of integers/floats"
    # check if matrix is list of lists
    if not isinstance(matrix, list):
        raise TypeError(message)
    elif not all(isinstance(row, list) for row in matrix):
        raise TypeError(message)

    # check if all rows are of the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # check if div is 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # nested list comp for new matrix
    new_mat = [[round(element / div, 2) for element in row] for row in matrix]
    return new_mat
