#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # Check the column on the left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True

def solve_nqueens(board, col, N, result):
    # Base case: If all queens are placed, print the solution
    if col >= N:
        result.append([[i, row.index(1)] for i, row in enumerate(board)])
        return True

    # Consider this column and try placing this queen in all rows
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            solve_nqueens(board, col + 1, N, result)

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove the queen from board[i][col]
            board[i][col] = 0

def nqueens(N):
    # Check if N is an integer
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board
    board = [[0 for _ in range(N)] for _ in range(N)]
    result = []

    # Solve the N queens problem
    solve_nqueens(board, 0, N, result)

    # Print the solutions
    for solution in result:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
