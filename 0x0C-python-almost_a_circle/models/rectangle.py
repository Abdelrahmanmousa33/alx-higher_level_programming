#!/usr/bin/python3
"""Defines a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """represent a rectangle"""

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
    def width(self, width):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """get the height of the Rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """set the height of the rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Set and get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, x):
        """" sets x of the rectnagle"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = x

    @property
    def y(self):
        """Set and get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, y):
        """set y of the rectangle"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = y
