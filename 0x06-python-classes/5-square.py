#!/usr/bin/python3
"""Defines a class Square."""


class Square:
    """Represents an empty square."""

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Returns or set the size of current square."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
