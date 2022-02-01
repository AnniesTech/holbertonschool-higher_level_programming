#!/usr/bin/python3
"""Class BaseGeometry and Class Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Instantiation with width and height: def __init__(self, width, height):
    width and height must be private. No getter or setter
    width and height must be positive integers,
    validated by integer_validator"""

    def __init__(self, width, height):
        """Initialization of width and height"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Method: area calculation"""
        return(self.__width * self.__height)

    def __str__(self):
        """Should print, and str() should return,
        the following rectangle description: [Rectangle] <width>/<height>"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
