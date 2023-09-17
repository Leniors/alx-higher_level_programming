#!/usr/bin/python3
"""creating a class square that inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """creating the class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update values of the rectangle"""
        if args:
            length = len(args)
            if length >= 1:
                self.id = args[0]
            if length >= 2:
                self.width = args[1]
                self.height = args[1]
            if length >= 3:
                self.x = args[2]
            if length >= 4:
                self.y = args[3]
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """dictionary rep of square"""
        return {'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y}
