#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mat = matrix[:]
    for num in range(len(matrix)):
        new_mat[num] = list(map(lambda x: x ** 2, matrix[num]))
    return (new_mat)
