#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Rep a class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """initialize the class"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """returns value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets value of size"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self, position):
        """returns values of a position"""
        return position

    @position.setter
    def position(self, position):
        """sets values of position"""
        if isinstance(position, tuple) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        elif isinstance(position[0], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif isinstance(position[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """get area of square"""
        return self.__size * self.__size

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for i in range(self.__position[1]):
                    print()
            for i in range(self.__size):
                for x in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        """prints the square"""
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            if i != self.__size - 1:
                print()
        return ""
