#!/usr/bin/python3
"""Class Square definition"""


class Square:
    """Class Square that defines a square:
        - Private instance attribute: size
        - Instantiation with optional size: def __init__(self, size=0)"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializer object"""
        self.size = size
        self.position = position

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
            for i in range(self.position[1]):
                print()
            for j in range(self.size):
                print(' ' * self.position[0], end="")
                print('#' * self.size)

    @property
    def position(self):
        """Property of position"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter of position"""
        if not isinstance(value, tuple) or len(value) != 2 \
           or not isinstance(value[0], int)\
           or not isinstance(value[1], int) \
           or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
