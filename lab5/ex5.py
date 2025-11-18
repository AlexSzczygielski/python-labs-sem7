#ex5.py
#random generator from ex2.py

from ex2 import random_generator
import numpy as np # for verify only

def multiply_matrices(arr1,arr2):
    num_cols1 = len(arr1[0])
    num_cols2 = len(arr2[0])
    num_rows1 = len(arr1)
    num_rows2 = len(arr2)

    if num_cols1 != num_rows2:
        raise ValueError ("Number of columns in the first matrix is not equal to the number of rows in the second matrix!")

    #i loop creates columns, j loop creates rows
    result = [[0 for i in range(num_cols2)] for j in range(num_rows1)]

    #i Row of arr1
    for i in range(num_rows1):
        #j Column of arr2
        for j in range(num_cols2):
            #k Rows of arr2
            for k in range(num_rows2):
                result[i][j] += arr1[i][k] * arr2[k][j]
    
    return result

def verify(matrix1, matrix2, result):
    #Verify
    np_1 = np.array(matrix1)
    np_2 = np.array(matrix2)
    np_multi = np.dot(np_1,np_2)
    np_result = np.array(result)

    return np.array_equal(np_result,np_multi), np_multi

if __name__ == "__main__":
    debug = False
    size = 8
    rand_range = 10000
    ### random generator already returns array of size 'size' ###
    matrix1 = [random_generator(size,rand_range) for i in range(size)]
    matrix2 = [random_generator(size,rand_range) for i in range(size)]

    result = multiply_matrices(matrix1,matrix2)

    #Verify
    success, np_multi = verify(matrix1,matrix2,result)


    print("Multiply two 8x8 matrices (generated randomly)\n" \
    f"Matrix 1: size {len(matrix1)} x {len(matrix1[0])} \n" \
    f"MATRIX 1: \n{matrix1 if debug else ''}\n" \
    f"Matrix 2: size {len(matrix2)} x {len(matrix2[0])} \n" \
    f"MATRIX 2: \n{matrix2 if debug else ''}\n" \
    f"sum_matrices(matrix1,matrix2):\n {result if debug else ''}\n" \
    f"np_multi: \n{np_multi if debug else ''}\n" \
    f"Verification is {'OK - SUCCESS' if success else 'NOT OK - FAILED'}")