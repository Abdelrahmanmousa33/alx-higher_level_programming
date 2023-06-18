#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    for num in range(len(matrix)):
        new_mat = list(map(lambda x: x ** 2, matrix[num]))
