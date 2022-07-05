#!/usr/bin/python3
"""Defines Student class"""


class Student():
    """Define a student"""

    def __init__(self, first_name, last_name, age):
        """Instanciation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if isinstance(attrs, list):
            return {key: value for key, value in
                    self.__dict__.items() if key in attrs}
        return self.__dict__
