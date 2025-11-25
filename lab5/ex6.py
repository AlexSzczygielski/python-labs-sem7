#ex6.py
#random generator from ex2.py

from ex2 import random_generator, colour
import numpy as np # for verify only


def compute_det(matrix):
    if len(matrix) != len(matrix[0]):
        raise ValueError("Matrix is not square")
    
    size = len(matrix) #matrix size
    
    #Base case for 2x2 matrix
    if size == 2:
        return matrix[0][0]*matrix[1][1] -  matrix[0][1]*matrix[1][0]
    
    #determinant
    det = 0
    for column in range(size):
        minor = [row[:column] + row[column+1:] for row in matrix[1:]] #skipping first row fo the matrix, all rows despite the column's
        det += ((-1)**column) * matrix[0][column] * compute_det(minor) #sign change * firsts row element * recursive (minor matrix)
    return det


def verify(matrix1, result):
    #Verify
    np_1 = np.array(matrix1)

    np_det = np.linalg.det(np_1)

    return np.isclose(result,np_det), np_det

if __name__ == "__main__":
    debug = True
    size = 5
    rand_range = 10
    ### random generator already returns array of size 'size' ###
    matrix1 = [random_generator(size,rand_range) for i in range(size)]

    result = compute_det(matrix1)

    #Verify
    success, np_det = verify(matrix1,result)


    print("Calculate determinant of a matrix (generated randomly)\n" \
    f"Matrix 1: size {len(matrix1)} x {len(matrix1[0])} \n" \
    f"MATRIX 1: \n{matrix1 if debug else ''}\n" \
    f"calculate_det(matrix1):\n {result if debug else ''}\n" \
    f"np_det: \n{np_det if debug else ''}\n" \
    f"Verification is {colour('green','OK - SUCCESS') if success else colour('red','NOT OK - FAILED')}")