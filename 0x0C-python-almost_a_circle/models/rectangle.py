#!/usr/bin/python3
"""Module for Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Representation of Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id_=None):
        """Initializes a new instance of the Rectangle class"""
        super().__init__(id_)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get The x-coordinate of the rectangle's position"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x-coordinate of the rectangle's position"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get The y-coordinate of the rectangle's position"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y-coordinate of the rectangle's position"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Displays the rectangle using ASCII art"""
        [print() for _ in range(self.y)]
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """Updates the attributes of the rectangle"""
        attribute_names = ['id', 'width', 'height', 'x', 'y']

        if args:
            for i, val in enumerate(args):
                if i < 5:
                    setattr(self, attribute_names[i], val)
            return
        for key, val in kwargs.items():
            if key in attribute_names:
                setattr(self, key, val)

    def to_dictionary(self):
        """Converts the rectangle object to a dictionary"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """Returns a string representation of the rectangle"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - " \
               f"{self.width}/{self.height}"
