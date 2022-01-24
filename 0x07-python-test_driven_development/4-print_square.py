#!/usr/bin/python3
""" This is 4-print_square.py that prints a square with the character #"""


def print_square(size):
    """Prints a square with the char "#"
        Return:
            the square printed
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is int:
        for i in range(size):
            print('#' * size)
