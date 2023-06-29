#!/usr/bin/python3
"""Defines a Square Class"""


class Square:
    """Simple class representing a square"""
    def __init__(self, size=0):
        """
        Initialize a person with the given name and age

        Args:
            size (int): Size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
