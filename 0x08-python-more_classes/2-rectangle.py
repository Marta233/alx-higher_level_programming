#!/usr/bin/python3
"""Define a Rectangle class."""


class Rectangle:
    """Represent rectangele."""

    def __init__(self, width=0, height=0):
        """Intialize a new rectangle
        Args:
            width (int): the width of the new rectangle. Defaults to 0.
            height (int): the width of the new rectangle.. Defaults to 0.
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """get/set the current Height of rectangle."""
        return(self.height)

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def width(self):
        """get/set current width of rectangle."""
        return(self.width)

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    def area(self):
        """To find the current rectangle
        Returns:
            int area: height * Width
        """
        return self.__width * self.__height

    def perimeter(self):
        """To finde the perimeter of the rectangle
        Returns:
            perimeter: 2 * (H + W)
        """
        return 2 * (self.__height + self.__width)
