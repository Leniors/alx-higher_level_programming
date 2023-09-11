#!/usr/bin/python3
"""
creating an empty class
named BaseGeometry
"""


class BaseGeometry:
    """implimenting the class"""

    def area(self):
        """area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer validator"""
        if isinstance(value, int) == False:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
