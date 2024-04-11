#!/usr/bin/python3
"""main fikle"""


import sys


def is_safe(board, row, col, N):
    """Check the column on the left side"""
    for i in range(col):
        if board[row][i]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def solve_nqueens(board, col, N, result):
    """Base case: If all queens are placed, print the solution"""
    if col >= N:
        result.append([[i, row.index(1)] for i, row in enumerate(board)])
        return True

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1

            solve_nqueens(board, col + 1, N, result)

            board[i][col] = 0


def nqueens(N):
    """Check if N is an integer"""
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    result = []

    solve_nqueens(board, 0, N, result)

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
