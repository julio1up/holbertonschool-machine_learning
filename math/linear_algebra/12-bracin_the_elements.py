#!/usr/bin/env python3
'''Bracing Elements Function'''



def np_elementwise(mat1, mat2):
    '''Bracing Elements Function'''
    add = mat1 + mat2
    sub = mat1 - mat2
    mul = mat1 * mat2
    div = mat1 / mat2
    return (add, sub, mul, div)
