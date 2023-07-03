#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Simple class representing Rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize a rectangle with the given width and height

        :param width: width of rectangle
        :param height: height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width

        :return: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """set the width

        :param value: of width

        :raises: TypeError: if value is not int
        :raises: ValueError: if width < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """get the height

        :return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """set the height

        :param value: of height

        :raises: TypeError: if value is not int
        :raises: ValueError: if height < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
