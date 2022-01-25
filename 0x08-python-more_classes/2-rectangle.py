#!/usr/bin/python3
"""Class Rectangle definition"""


class Rectangle:
    """Class Rectangle  that defines a Rectangle :
        - Private instance attribute: width
        - Private instance attribute: height
        - Instantiation with optional width and
        height: def __init__(self, width=0, height=0)"""

    def __init__(self, width=0, height=0):
        """Atributes of the object"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Property of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Public instance method:
            - Return: the current rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """Public instance method:
            - Return: the current rectangle perimeter"""
        return (self.__width + self.__width) + (self.__height + self.__height)
