#!/usr/bin/python3
"""Module for MyList class"""


class MyList(list):
    """Sub-Class from list"""
    def print_sorted(self):
        """Print sorted list"""
        print(sorted(self))
