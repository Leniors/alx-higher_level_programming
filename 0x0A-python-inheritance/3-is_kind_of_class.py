#!/usr/bin/python3
"""
define function that checks for instance or subclass
"""


def is_kind_of_class(obj, a_class):
    """implimenting the function"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
