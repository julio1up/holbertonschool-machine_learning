#!/usr/bin/env python3
'''Line Up Function'''


def add_arrays(vec1, vec2):
    '''Line Up Function'''
    result = []
    if(len(vec1) != len(vec2)):
        return None
    for i in range(len(vec1)):
        result.append(vec1[i] + vec2[i])
    return result


arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
add_arrays(arr1, arr2)
add_arrays(arr1, [1, 2, 3])
