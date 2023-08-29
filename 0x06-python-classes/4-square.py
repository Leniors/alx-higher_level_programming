#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Rep a class Square"""
    def __init__(self, size=0):
        """initialize the class"""
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """get area of square"""
        return self.__size * self.__size
