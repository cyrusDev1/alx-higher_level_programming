#!/usr/bin/python3
"""Solves the N-queens puzzle."""


import sys


def init_chessboard(n):
    """Initialize an n * n sized chessboard."""
    board = []
    for i in range(n):
        board.append([])
    for row in board:
        for i in range(n):
            row.append(' ')
    return (board)


def copy_board(board):
    """Return a copy of chessboard"""
    if isinstance(board, list):
        return list(map(copy_board, board))
    return board


def get_queens(board):
    """Return position of queens"""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def redraw(board, row, col):
    """Redraw a chessboard.

    Args:
        board (list): the current chessboard.
        row (int): the row where a queen was last played.
        col (int): the column where a queen was last played.
    """
    for c in range(col + 1, len(board)):
        board[row][c] = "X"
    for c in range(col - 1, -1, -1):
        board[row][c] = "X"
    for r in range(row + 1, len(board)):
        board[r][col] = "X"
    for r in range(row - 1, -1, -1):
        board[r][col] = "X"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "X"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "X"
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "X"
        c -= 1


def recursive(board, row, queens, solutions):
    """Solve an N-queens
    Args:
        board (list): the current chessboard
        row (int): the current row
        queens (int): the current number of placed queens
        solutions (list): lists of solutions
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_queens(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == " ":
            temp_board = copy_board(board)
            temp_board[row][c] = "Q"
            redraw(temp_board, row, c)
            solutions = recursive(temp_board, row + 1, queens + 1, solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_chessboard(int(sys.argv[1]))
    solutions = recursive(board, 0, 0, [])
    for i in solutions:
        print(i)
