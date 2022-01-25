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
        return self.width * self.height

    def perimeter(self):
        """Public instance method:
            - Return: the current rectangle perimeter"""
        if self.width <= 0 or self.height <= 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Prints a Rectangle"""
        result = ""
        if self.width <= 0 or self.height <= 0:
            return result
        else:
            for i in range(self.height):
                for j in range(self.width):
                    result += "#"
                if (i != (self.height - 1)):
                    result = result + "\n"
        return result

    def __repr__(self):
        """Method that returns a representation of str"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Method that prints a message when instance is deleted"""
        print("Bye rectangle...")
