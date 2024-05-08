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

  rows, cols = len(grid), len(grid[0])
  perimeter = 0

  # Iterate through each cell in the grid
  for row in range(rows):
    for col in range(cols):
      # Check if the current cell is land (1)
      if grid[row][col] == 1:
        # Count the edges bordering water
        perimeter += 4  # Assume all sides are water initially

        # Check left neighbor (if not within bounds or water, count edge)
        if col - 1 < 0 or grid[row][col - 1] == 0:
          perimeter -= 1

        # Check right neighbor (if not within bounds or water, count edge)
        if col + 1 >= cols or grid[row][col + 1] == 0:
          perimeter -= 1

        # Check top neighbor (if not within bounds or water, count edge)
        if row - 1 < 0 or grid[row - 1][col] == 0:
          perimeter -= 1

        # Check bottom neighbor (if not within bounds or water, count edge)
        if row + 1 >= rows or grid[row + 1][col] == 0:
          perimeter -= 1

  return perimeter
