#ex3.py

def dot_product(arr1,arr2):
    #Approach without numpy
    if len(arr1)>len(arr2):
        for element in range(len(arr1)-len(arr2)):
            arr2.append(0)

    if len(arr2)<len(arr1):
        for element in range(len(arr2)-len(arr1)):
            arr1.append(0)
        
    result = 0
    for i, element in enumerate(arr1):
        result += element*arr2[i]

    return result

if __name__ == "__main__":
    arr1 = [1, 2, 12, 4]
    arr2 = [2, 4, 2, 8]

    print(f"Scalar product of vectors {arr1} and {arr2} is:\n {dot_product(arr1,arr2)}")