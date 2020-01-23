from copy import deepcopy
from random import randint

def quick_sort(array):
    arr = deepcopy(array)
    quick_sort_helper(arr, 0, len(arr)-1)
    return arr

def quick_sort_helper(arr, start, end):
    if start < end:
        pivot = partition_sort(arr, start, end)
        quick_sort_helper(arr, start, pivot-1)
        quick_sort_helper(arr, pivot+1, end)

def partition_sort(arr, start, end):
    pivot_value = arr[randint(start, end)]
    i = start + 1
    j = start + 1
    
    while j <= end: 
        if arr[j] < pivot_value:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1

    arr[start], arr[i-1] = arr[i-1], arr[start]

    return i-1
