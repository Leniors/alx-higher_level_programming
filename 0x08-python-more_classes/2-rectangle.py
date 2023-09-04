#!/usr/bin/python3
"""module creating a Rectangle class"""


class Rectangle:
    """defining the class"""

    def __init__(self, width=0, height=0):
        """initializes the class Rectangle"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """gets width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """gets height of a circle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of the rectangle"""
        return self.__width + self.__height + self.__width + self.__height
