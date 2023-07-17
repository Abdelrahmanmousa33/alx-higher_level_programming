#!/usr/bin/python3

"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize new rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """get the width of the Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the width of the recatnagle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get the height of the Rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """set the height of the rectangle"""

        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set and get the x coordinate of the Rectangle."""

        return self.__x

    @x.setter
    def x(self, value):
        """" sets x of the rectnagle"""

        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set and get the y coordinate of the Rectangle."""

        return self.__y

    @y.setter
    def y(self, value):
        """set y of the rectangle"""

        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
