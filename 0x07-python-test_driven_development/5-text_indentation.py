#!/usr/bin/python3
"""
defining a function that tests indentation
it takes a text as an argument
checks for char: ".", "?" and ":"
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    length = len(text)

    for ch in text:
        print(ch, end="")
        if ch == "." or ch == "?" or ch == ":":
            print("\n")
