#!/usr/bin/python3
"""
create a class square
inherits from class rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """define class square"""

    def __init__(self, size):
        """initializer"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """str"""
        return f"[Square] {self.__size}/{self.__size}"
