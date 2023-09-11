#!/usr/bin/python3
"""
defining a class that inherits from list
"""


class MyList(list):
    """
    implimrnting the function
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
