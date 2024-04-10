#!/usr/bin/python3
"""non-attacking queens on an N×N"""


import sys


def is_safe(board, row, col):
  """
  Checks if placing a queen at (row, col) is safe (doesn't attack other queens).
  """
  # Check row on left side
  for i in range(col):
    if board[row][i] == 1:
      return False
  
  # Check upper diagonal on left side
  i, j = row, col
  while i >= 0 and j >= 0:
    if board[i][j] == 1:
      return False
    i -= 1
    j -= 1

  # Check lower diagonal on right side
  i, j = row, col
  while i < len(board) and j >= 0:
    if board[i][j] == 1:
      return False
    i += 1
    j -= 1
  return True

def solve_n_queens(board, col):
  """
  Solves the N queens problem using backtracking.
  """
  if col >= len(board):
    # All queens placed successfully, print the solution
    solution = []
    for i in range(len(board)):
      for j in range(len(board)):
        if board[i][j] == 1:
          solution.append([i, j])
    print(solution)
    return

  for i in range(len(board)):
    # Check if current row and col are safe
    if is_safe(board, i, col):
      board[i][col] = 1  # Place queen
      solve_n_queens(board, col + 1)  # Recursively solve for next col
      board[i][col] = 0  # Backtrack, remove queen

def main():
  """
  Main function to handle program arguments and solve the puzzle.
  """
  if len(sys.argv) != 2:
    print("Usage: nqueens N", file=sys.stderr)
    sys.exit(1)

  try:
    n = int(sys.argv[1])
  except ValueError:
    print("N must be a number", file=sys.stderr)
    sys.exit(1)

  if n < 4:
    print("N must be at least 4", file=sys.stderr)
    sys.exit(1)

  # Initialize chessboard with all empty squares (0)
  board = [[0 for _ in range(n)] for _ in range(n)]
  solve_n_queens(board, 0)

if __name__ == "__main__":
  main()

