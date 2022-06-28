#!/usr/bin/python3
"""Defines function that print a square"""


def print_square(size):
    """Prints a square"""
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for i in range(size):
            print("#", end="")
        print("")
