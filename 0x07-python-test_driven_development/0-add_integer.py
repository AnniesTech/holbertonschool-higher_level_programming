#!/usr/bin/python3
""" This is 0-add_integer that adds 2 integers"""


def add_integer(a, b=98):
    """ Returns the addition of two numbers:
        a (int or float): first value
        b (int or float): second value
        Return:
            the addition of a and b
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(a) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
