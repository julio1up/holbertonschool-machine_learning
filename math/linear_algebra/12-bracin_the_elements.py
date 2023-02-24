#!/usr/bin/env python3
'''Bracing Elements Function'''



def np_elementwise(mat1, mat2):
    '''Bracing Elements Function'''
    add = add(mat1, mat2)
    sub = subtract(mat1, mat2)
    mul = multiply(mat1, mat2)
    div = divide(mat1, mat2)
    return (add, sub, mul, div)
