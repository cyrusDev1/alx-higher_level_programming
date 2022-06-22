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

    def __eq__(self, other):
        """Equal : =="""
        return self.area() == other.area()
    
    def __ne__(self, other):
        """Not equal : !="""
        return self.area() != other.area()
    
    def __lt__(self, other):
        """less than : <"""
        return self.area() < other.area()
    
    def __le_(self, other):
        """less than or equal: <="""
        return self.area() <= other.area()

    def __gt__(self, other):
        """great than : >"""
        return self.area() > other.area()

    def __ge__(self, other):
        """great than or equal : >="""
        return self.area() >= other.area()
