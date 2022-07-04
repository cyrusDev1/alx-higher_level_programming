#!/usr/bin/python3
"""Defines MyList class"""


class MyList(list):
    """MyList class inherits frm list"""
    def print_sorted(self):
        new = self[:]
        new.sort()
        print(new)
