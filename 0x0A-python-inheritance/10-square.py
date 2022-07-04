#!/usr/bin/python3
"""Defines Square class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square class"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        # or Rectangle.__init__(self, size, size)
