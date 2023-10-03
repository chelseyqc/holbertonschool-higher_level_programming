#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # nested list comprehension
    # outer loop: iterates over each row in the input matrix
    # inner loop: iterates over each element in the current row
    return [[x ** 2 for x in row] for row in matrix]
