#!/usr/bin/python3
"""module creating a Rectangle class"""


class Rectangle:
    """defining the class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """initializes the class Rectangle"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """gets width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of Rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """gets height of a circle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the Rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of the rectangle"""
        return self.__width + self.__height + self.__width + self.__height

    def __str__(self):
        """returns the string of Rectangle"""
        if self.__width == 0 or self.height == 0:
            return ""
        rect_str = ""

        for i in range(self.height):
            rect_str += str(self.print_symbol) * self.__width
            if i < self.__height - 1:
                rect_str += "\n"
        return rect_str

    def __repr__(self):
        """returns string representaion"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """delete the Rectangle"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        a = rect_1.area()
        b = rect_2.area()
        if a >= b:
            return rect_1
        else:
            return rect_2
