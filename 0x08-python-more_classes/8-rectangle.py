#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Simple class representing Rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with the given width and height

        :param width: width of rectangle
        :param height: height of rectangle
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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

    def area(self):
        """Compute the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Compute the perimeter of the rectangle"""
        return (0 if self.__height == 0 or self.__width == 0
                else 2 * (self.__width + self.__height))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest object based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __str__(self):
        """Informal and nicely printable string representation of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ""
        return '\n'.join(
            [str(self.print_symbol) * self.__width] * self.__height
        )

    def __repr__(self):
        """Official string representation of rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """deletes instance of Rectangle class, and prints "bye" message"""
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
