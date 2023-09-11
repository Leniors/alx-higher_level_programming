#!/usr/bin/python3
"""
creating a function that compares two objects and see if they are the same
"""


def is_same_class(obj, a_class):
    """implimenting the function"""
    if type(obj) == a_class:
        return True
    return False
