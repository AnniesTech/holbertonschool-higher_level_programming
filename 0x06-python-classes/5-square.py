#!/usr/bin/python3
"""Class Square definition"""


class Square:
    """Class Square that defines a square:
        - Private instance attribute: size
        - Instantiation with optional size: def __init__(self, size=0)"""

    def __init__(self, size=0):
        """Initializer object"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Public instance method:
            - Return: the current square area"""
        return self.__size ** 2

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

    def my_print(self):
        """Prints a square"""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print('#' * self.size)
