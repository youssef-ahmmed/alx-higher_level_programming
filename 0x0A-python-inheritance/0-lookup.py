#!/usr/bin/python3
"""Module for `lookup()` function"""


def lookup(obj):
    """function that returns the list of available
        attributes and methods of an object"""
    return list(dir(obj))
