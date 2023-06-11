#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    n = len(matrix)
    for i in range(n):
        n = len(matrix[i])
        for j in range(n):
            print('{:d}'.format(matrix[i][j]), end=' ') if j != n - 1 \
                                else print('{:d}'.format(matrix[i][j]))
