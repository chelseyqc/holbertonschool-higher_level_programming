#!/usr/bin/python3
"""pascal's triangle"""


def pascal_triangle(n):
    """returns a list of integers representing the Pascal's triangle of n"""
    list = []
    if n <= 0:
        return list

    triangle = [[1]]
    for row_index in range(1, n):
        current_row = [1]
        previous_row = triangle[row_index - 1]

        for element_index in range(1, row_index):
            current_row.append(previous_row[element_index - 1]
                                + previous_row[element_index])
        current_row.append(1)

        triangle.append(current_row)
    return triangle
