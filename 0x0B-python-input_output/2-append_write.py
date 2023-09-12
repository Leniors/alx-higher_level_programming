#!/usr/bin/python3
"""function to append to a text file"""


def append_write(filename="", text=""):
    """implimenting the function"""
    with open(filename, mode="a", encoding="utf-8") as f:
        written = f.write(text)
        return written
