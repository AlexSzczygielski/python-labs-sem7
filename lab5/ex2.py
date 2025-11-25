#ex2.py
#Sorting numbers

import random

def partition_descent(arr, low, high):
    #implements partition logic required for quick sort
    #selects last element as the pivot
    #returns an index of pivot after partitioning
    pivot = arr[high]
    i = low - 1
    for j in range (low,high):
        if arr[j] >= pivot: #greater or equal to the left
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quick_sort_descent(arr, low, high):
    #recursion approach, operating on the 'arr' reference (no arr copy, no return)
    #arr - array
    #low, high - range of arr that should be sorted
    if low < high:
        p = partition_descent(arr, low, high) #index
        quick_sort_descent(arr, low, p-1) #left side
        quick_sort_descent(arr, p+1, high) #right side

def random_generator(arr_len, rand_range):
    #returns random array in the arr_len length and range of -rand_range to +rand_range
    data = []
    for i in range(arr_len):
        data.append(random.randint(-rand_range, +rand_range))
    return data

def colour(col,text):
    #Colour text using ANSI escape sequence
    RED = "\033[31m"
    GREEN = "\033[32m"
    STANDARD = "\033[0m"
    match col:
        case "red":
            return RED + text + STANDARD
        case "green":
            return GREEN + text + STANDARD
        case _:
            return text


if __name__ == "__main__":
    #config
    arr_len = 50
    rand_range = 1000
    arr = random_generator(arr_len, rand_range)
    arr_cp = arr.copy()

    #sorting
    quick_sort_descent(arr, 0, len(arr) - 1) #Sorting with my function
    arr_cp.sort(reverse=True) #Built in method for checking

    #results
    if arr == arr_cp:
        print(f"Success! Sorting in descending order completed. {colour('green','Verification OK')}")
    else:
        print(f"{colour('red','Verification failed')}, sorted array and verification arrays are not equal.")

    print(f"Sorted array: {arr}")