#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle():
    """Represents an empty rectangle."""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Set or get width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set or get height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns area of rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)

    def __str__(self):
        """the rectangle with the character #"""
        rectangle = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle
        for h in range(self.__height):
            for w in range(self.__width):
                rectangle += "#"
            if h != self.__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        """return a string representation of the rectangle to be able
        to recreate a new instance by using
        """
        return ('Rectangle(' + str(self.__width) + ', '
                + str(self.__height) + ')')

    def __del__(self):
        """Print the message Bye rectangle... (... being 3 dots not ellipsis)
        when an instance of Rectangle is deleted
        """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
