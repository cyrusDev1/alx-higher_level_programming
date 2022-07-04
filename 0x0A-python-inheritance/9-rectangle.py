#!/usr/bin/python3
"""Defines Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectanle class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area of rectanle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Returns description of obj"""
        return ("[{}] {}/{}".format(self.__class__.__name__, self.__width,
                                    self.__height))
