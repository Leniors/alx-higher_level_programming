#!/usr/bin/python3
"""function to read a file"""


def read_file(filename=""):
    """implimenting the function"""
    with open(filename, mode="r") as f:
        print(f.read(), end="")
