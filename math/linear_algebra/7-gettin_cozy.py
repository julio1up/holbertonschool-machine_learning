#!/usr/bin/env python3
'''Gettin Cozy Function'''


def cat_matrices2D(mat1, mat2, axis=0):
    '''Gettin Cozy'''
    new_matrix = []
    if axis == 0:
        if len(mat1[0]) != len(mat2[0]):
            return None
        new_matrix = mat1 + mat2
    elif axis == 1:
        if len(mat1) != len(mat1):
            return None
        new_matrix = [mat1[i]+mat2[i] for i in range(len(mat1))]
    else:
        return None
    return new_matrix
