#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle:
    """Represent rectangele."""

    def __init__(self, width=0, height=0):
        """Intialize a new rectangle
        Args:
            width (int): the width of the new rectangle.
            height (int): the width of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """get/set current width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get/set the current Height of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
