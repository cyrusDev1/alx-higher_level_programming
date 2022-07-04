#!/usr/bin/python3
"""Defines add_attribute function"""


def add_attribute(obj, atr, val):
    """Set attribute if it is possible"""
    if hasattr(obj, '__dict__'):
        setattr(obj, atr, val)
    else:
        raise TypeError("can't add new attribute")
