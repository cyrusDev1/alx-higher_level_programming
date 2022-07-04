#!/usr/bin/python3
"""Defines Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a rectanle class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns area of rectanle"""
        return (self.__size ** 2)

    def __str__(self):
        """Returns description of obj"""
        return ("[{}] {}/{}".format(self.__class__.__name__, self.__size,
                                    self.__size))
