#!/usr/bin/python3
class Square:
    """
    Square - a square is a shape with four sides that have equal length
    """
    def __init__(self, size=0):
        try:
            if isinstance(size, int) == False:
                raise TypeError
            elif size < 0:
                raise ValueError
            self.__size = size
        except TypeError:
            print("size must be an integer")
            return
        except ValueError:
            print("size must be >= 0")
            return
