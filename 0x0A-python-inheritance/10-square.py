#!/usr/bin/python3
"""Class BaseGeometry and Class Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Rectangle"""

    def __init__(self, size):
        """Instantiation with size: def __init__(self, size)::
        size must be private. No getter or setter
        size must be a positive integer, validated by integer_validator"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method: area calculation"""
        return self.__size ** 2
