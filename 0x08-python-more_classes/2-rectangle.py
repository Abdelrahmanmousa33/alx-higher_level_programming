#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """ initate optional width and height"""

        self.height = height
        self.width = width

    @property
    def width(self):
        """gets width attribute"""

        return (self.__width)

    @width.setter
    def width(self, value):
        """ sets the width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""

        return self.__height

    @height.setter
    def height(self, value):
        """ sets the hegith"""

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return the are"""

        return (self.width * self.height)

    def perimeter(self):
        """ retturn the perimeter"""

        return ((self.__width * 2) + (self.__height * 2))
