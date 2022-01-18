#!/usr/bin/python3
"""Class Square definition"""

class Square:
    """Class Square that defines a square:
        - Private instance attribute: size
        - Instantiation with optional size: def __init__(self, size=0)"""

    def __init__(self, size=0):
        """Initialite Size as a private attribute"""
        self.size = size

    def __mq__(self, other):
        """ > """
        return self.area() > other.area()

    def __mi__(self, other):
        """ >= """
        return self.area() >= other.area()

    def __mei__(self, other):
        """ <= """
        return self.area() <= other.area()

    def __meq__(self, other):
        """ <  """
        return self.area() < other.area()

    def __ig__(self, other):
        """ == """
        return self.area() == other.area()

    def __dif__(self, other):
        """ != """
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
            - Return: the current square area"""
        return self.__size ** 2
