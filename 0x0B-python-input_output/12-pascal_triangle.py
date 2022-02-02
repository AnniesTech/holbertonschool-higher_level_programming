#!/usr/bin/python3
"""function that returns a list of lists of integers
    representing the Pascal’s triangle of n"""

def pascal_triangle(n):
    if n > 0:
        for fila in range(1, n + 1):
            for columna in range(1, fila + 1):
                print(columna, end="")
        print()
    if n < 0:
        new_list = []
        return new_list
