#ex3.py
import numpy as np #verification
from ex2 import colour

def dot_product(arr1,arr2):
    #Approach without numpy

    #Append zeros preparation
    if len(arr1)>len(arr2): 
        for element in range(len(arr1)-len(arr2)):
            arr2.append(0)

    if len(arr2)>len(arr1):
        for element in range(len(arr2)-len(arr1)):
            arr1.append(0)

    #dot_product    
    result = 0
    for i, element in enumerate(arr1):
        result += element*arr2[i]

    return result

def verify(arr1, arr2):
    a = np.array(arr1)
    b = np.array(arr2)

    return np.dot(a, b)

if __name__ == "__main__":
    arr1 = [1, 2, 12, 4]
    arr2 = [2, 4, 2, 8]

    dot_prod = dot_product(arr1,arr2)
    print(f"Scalar product of vectors {arr1} and {arr2} is:\n {dot_prod}")

    dot_verify = verify(arr1,arr2)

    #results
    if dot_prod == dot_verify:
        print(f"Success! {colour('green','Verification OK')}")
    else:
        print(f"{colour('red','Verification failed')}")