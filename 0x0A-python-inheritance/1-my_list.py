#!/usr/bin/python3
"""Defines MyList class"""


class MyList(list):
    """MyList class inherits frm list"""
    def print_sorted(self):
        print(sorted(self))
