#!/usr/bin/python3
""" 3d array"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island in a grid.
    Args:
    grid: A list of lists of integers representing the grid.
    - 0 represents water.
    - 1 represents land.
    Returns:
    The perimeter of the island (integer).
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                # Check left neighbor
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

                # Check top neighbor
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

    return perimeter
