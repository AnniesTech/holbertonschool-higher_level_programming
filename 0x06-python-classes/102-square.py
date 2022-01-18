#!/usr/bin/python3
"""Class Square definition"""


class Square:
    """Class Square that defines a square:
        - Private instance attribute: size
        - Instantiation with optional size: def __init__(self, size=0)"""
    def __init__(self, size=0):
        """Initialize Size as a private attribute"""
        self.size = size

    def __gt__(self, other):
        """ > """
        return self.area() > other.area()

    def __ge__(self, other):
        """ >= """
        return self.area() >= other.area()

    def __le__(self, other):
        """ <= """
        return self.area() <= other.area()

    def __lt__(self, other):
        """ <  """
        return self.area() < other.area()

    def __eq__(self, other):
        """ Method == """
        return self.area() == other.area()

    def __ne__(self, other):
        """ Method != """
        return self.area() != other.area()

    @property
    def size(self):
        """Property of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter of size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Public instance method:
           * Return: the current square area"""
        return self.__size ** 2
