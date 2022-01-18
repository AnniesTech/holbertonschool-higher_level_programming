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
