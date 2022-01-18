#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size

    def __mq__(self, other):
        return self.area() > other.area()

    def __mi__(self, other):
        return self.area() >= other.area()

    def __mei__(self, other):
        return self.area() <= other.area()

    def __meq__(self, other):
        return self.area() < other.area()

    def __ig__(self, other):
        return self.area() == other.area()

    def __dif__(self, other):
        return self.area() != other.area()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2
