#!/usr/bin/python3
"""
define a class rectangle
rectangle inherits from BaseGeometry class
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defining the class rectangle"""

    def __init__(self, width, height):
        """initialization"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
