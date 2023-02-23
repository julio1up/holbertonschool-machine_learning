#!/usr/bin/env python3
'''Transpose Function'''


def matrix_transpose(matrix):
    '''Transpose Function'''
    result=[]
    current_array=[]
    for j in range(0,len(matrix[0])):
        current_array=[[i[j] for i in matrix]]
        result= result+current_array
        return result

mat1 = [[1, 2], [3, 4]]
matrix_transpose(mat1)
mat2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]
matrix_transpose(mat2)
