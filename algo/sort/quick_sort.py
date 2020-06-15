# Quick sort algorithm
from random import randint

def quick_sort(array):
    arr = array.copy()
    quick_sort_helper(arr, 0, len(arr)-1)
    return arr

def quick_sort_helper(arr, start, end):
    if start < end:
        pivot = partition_sort(arr, start, end)
        quick_sort_helper(arr, start, pivot-1)
        quick_sort_helper(arr, pivot+1, end)

def partition_sort(arr, start, end):
    pivot = start
    i = start+1
    j = end

    done = False
    while not done:
        while i <= j and arr[i] <= arr[pivot]:
            i += 1
        while j >= i and arr[j] >= arr[pivot]:
            j -= 1
    
        if j < i:
            done = True
        else:
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[j], arr[pivot] = arr[pivot], arr[j]
    
    return j
    
def partition_sort_2(arr, start, end):
    pivot = start
    i = start+1
    j = start+1
    
    while j <= end: 
        if arr[j] < arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        j += 1

    arr[start], arr[i-1] = arr[i-1], arr[start]

    return i-1
