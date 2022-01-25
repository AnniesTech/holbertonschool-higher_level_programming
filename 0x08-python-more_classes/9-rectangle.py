#!/usr/bin/python3
"""Class Rectangle definition"""


class Rectangle:
    """Class Rectangle  that defines a Rectangle :
        - Private instance attribute: width
        - Private instance attribute: height
        - Instantiation with optional width and
        height: def __init__(self, width=0, height=0)"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Atributes of the object"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        symbol = str(self.print_symbol)
        if self.width <= 0 or self.height <= 0:
            return result
        else:
            for i in range(self.height):
                for j in range(self.width):
                    result += symbol
                if (i != (self.height - 1)):
                    result = result + "\n"
        return result

    def __repr__(self):
        """Method that returns a representation of str"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Method that prints a message when instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            rect_2

    @classmethod
    def square(cls, size=0):
        """Class Method that returns a new Rectangle instance"""
        return cls(size, size)
