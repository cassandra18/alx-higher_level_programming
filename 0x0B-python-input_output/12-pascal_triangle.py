#!/usr/bin/python3
"""The pascal_triangle module"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle of n

    Args:
        n(int): number of rows
    """
    if n <= 0:
        return []

    pascal_triangle = [[1]]

    for i in range(1, n):
        firstRow = pascal_triangle[i - 1]
        nextRow = [1]

        for j in range(1, i):
            output = firstRow[j - 1] + firstRow[j]
            nextRow.append(output)

        nextRow.append(1)
        pascal_triangle.append(nextRow)

    return pascal_triangle
