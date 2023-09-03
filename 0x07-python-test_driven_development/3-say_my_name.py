#!/usr/bin/python3
"""
defining a function that returns a full name
Args:
firstname and lastname
"""

def say_my_name(first_name, last_name=""):
    """
    implimenting the function
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name == "":
        print("My name is {}".format(last_name))
        return
    if last_name == "":
        print("My name is {}".format(first_name))
        return
    print("My name is {} {}".format(first_name, last_name))
