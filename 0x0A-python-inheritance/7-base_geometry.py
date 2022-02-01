#!/usr/bin/python3
"""Class BaseGeometry definition"""


class BaseGeometry():
    """Class BaseGeometry:
        - Public instance method: def area(self): Raise exeption
        - Public instance method: def integer_validator(self, name, value)"""

    def area(self):
        """Function that raises an Exception with a message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates if value is an integer and name is a string"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
