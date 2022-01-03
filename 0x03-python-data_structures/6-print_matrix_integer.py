#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is not None:
        for lista in matrix:
            print(' '.join('{:d}'.format(item) for item in lista))
