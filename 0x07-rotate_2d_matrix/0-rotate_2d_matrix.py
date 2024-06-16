#!/usr/bin/python3
"""rotate_2d_matrix module"""


def transpose_matrix(matrix, n):
    """
    transpose_matrix
    Args:
        matrix: 2d matrix
    """
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    """
    reverse_matrix
    Args:
        matrix: 2d matrix
    """
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    """rotate_2d_matrix
    Args:
        matrix: 2d matrix
    """
    n = len(matrix)

    transpose_matrix(matrix, n)
    reverse_matrix(matrix)

    return matrix
