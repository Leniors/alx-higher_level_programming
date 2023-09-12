#!/usr/bin/python3
"""function to write to a file"""


def write_file(filename="", text=""):
    """implimenting the function"""
    with open(filename, mode="w", encoding="utf-8") as f:
        written = f.write(text)
        return written
