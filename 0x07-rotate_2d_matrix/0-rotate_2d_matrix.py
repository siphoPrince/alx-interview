#!/usr/bin/python3
"""main base code for 2d rotate"""


def rotate_2d_matrix(matrix):
    n = len(matrix)
    # Swap elements layer by layer
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            # Save top element
            top = matrix[first][i]
            # Move left to top
            matrix[first][i] = matrix[-i - 1][first]
            # Move bottom to left
            matrix[-i - 1][first] = matrix[-first - 1][-i - 1]
            # Move right to bottom
            matrix[-first - 1][-i - 1] = matrix[i][-first - 1]
            # Move top to right
            matrix[i][-first - 1] = top
