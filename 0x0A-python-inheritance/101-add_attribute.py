#!/usr/bin/python3
"""Defines add_attribute function"""


def add_attribute(obj, atr, val):
    """"""
    if hasattr(obj, '__dict__'):
        setattr(obj, atr, val)
    else:
        raise Exception("can't add new attribute")
