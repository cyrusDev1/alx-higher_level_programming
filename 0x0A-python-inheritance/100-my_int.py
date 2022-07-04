#!/usr/bin/python3
"""Defines class MyInt"""


class MyInt(int):
    """Reverse == and !="""

    def __eq__(self, other):
        """Reverse =="""
        return super().__ne__(other)

    def __ne__(self, other):
        """Reverse !="""
        return super().__eq__(other)
