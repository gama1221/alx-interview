#!/usr/bin/python3
""" -*- coding: rotate matrix """


def rotate_2d_matrix(matrix) -> None:
    """ rotate matrix - transpose """
    N = len(matrix)
    for row in range(N):
        new = []
        for col in range(N - 1, -1, -1):
            new.append(matrix[col][row])
        matrix.append(new)
    [matrix.pop(0) for i in range(N)]
