#!/usr/bin/python3
"""trianglge"""


def pascal_triangle(n):
    """
    This function generates Pascal's triangle up
    to the given number of rows (n).

    Args:
        n: The number of rows to generate in the Pascal's triangle.

    Returns:
        A list of lists representing the Pascal's
        triangle. Returns an empty list if n <= 0.
    """

    if n <= 0:
        return []

    triangle = [[1], [1, 1]]

    for row in range(2, n):
        new_row = [1]
        for col in range(1, row):
            new_row.append(triangle[row - 1][col - 1] + triangle[row - 1][col])
        new_row.append(1)
        triangle.append(new_row)

    return triangle


def print_pascal_triangle(triangle):
    """
    Prints the Pascal's triangle in the desired format.
    """
    for row in triangle:
        print(" ".join(map(str, row)))
