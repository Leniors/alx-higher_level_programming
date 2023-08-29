#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Rep a class Square"""
    def __init__(self, size=0):
        """initialize the class"""
        try:
            if isinstance(size, int) is False:
                raise TypeError
            elif size < 0:
                raise ValueError
            self.__size = size
        except TypeError:
            print("size must be an integer")
            return
        except ValueError:
            print("size must be >= 0")
            return
