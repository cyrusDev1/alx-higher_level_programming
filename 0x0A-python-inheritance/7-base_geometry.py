#!/usr/bin/python3
"""Defines BaseGeeomtry class"""


class BaseGeometry():
    """Represent base geometry"""

    def area(self):
        """Raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value

        Args:
            name (str): Name of param
            value (int): Param to look at
        Raises:
            TypeError: if value is not integer
            ValueError: if value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
