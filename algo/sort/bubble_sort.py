# Bubble sort algorithm

def bubble_sort(arr):
    array = arr.copy()
    n = len(array) - 1
    while n:
        checks = 0
        for i in range(n):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                checks += 1
        n -= 1
        if checks == 0:
            break
    return array
