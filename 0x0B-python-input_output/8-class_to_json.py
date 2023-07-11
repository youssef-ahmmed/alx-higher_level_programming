#!/usr/bin/python3
"""Module for `class_to_json` function"""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure"""
    return obj.__dict__
