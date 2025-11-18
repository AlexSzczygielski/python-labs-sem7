#ex4.py
#random generator from ex2.py

from ex2 import random_generator
import numpy as np # for verify only

def sum_matrices(arr1,arr2):
    size = len(arr1)
    return [[arr1[i][j] + arr2[i][j] for j in range(size)] for i in range(size)]

def verify(matrix1, matrix2, result):
    #Verify
    np_1 = np.array(matrix1)
    np_2 = np.array(matrix2)
    np_sum = np_1 + np_2
    np_result = np.array(result)

    return np.array_equal(np_result,np_sum), np_sum

if __name__ == "__main__":
    debug = False
    size = 128
    rand_range = 10000
    ### random generator already returns array of size 'size' ###
    matrix1 = [random_generator(size,rand_range) for i in range(size)]
    matrix2 = [random_generator(size,rand_range) for i in range(size)]

    result = sum_matrices(matrix1,matrix2)

    #Verify
    success, np_sum = verify(matrix1,matrix2,result)


    print("Sum two 128x128 matrices (generated randomly)\n" \
    f"Matrix 1: size {len(matrix1)} x {len(matrix1[0])} \n" \
    f"MATRIX 1: \n{matrix1 if debug else ''}\n" \
    f"Matrix 2: size {len(matrix2)} x {len(matrix2[0])} \n" \
    f"MATRIX 2: \n{matrix2 if debug else ''}\n" \
    f"sum_matrices(matrix1,matrix2):\n {result if debug else ''}\n" \
    f"np_sum 2: \n{np_sum if debug else ''}\n" \
    f"Verification is {'OK - SUCCESS' if success else 'NOT OK - FAILED'}")