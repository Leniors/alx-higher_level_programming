#!/usr/bin/python3
"""creating a class named Base"""


class Base:
    """implimrnting the class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
