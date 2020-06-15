# Insertion sort algorithm

def insertion_sort(arr):
    array = arr.copy()
    arr_len = len(array)
    for i in range(1, arr_len):
        temp = array[i]
        j = i-1
        while j >= 0:
            if array[j] > temp:
                array[i] = array[j]
                i -= 1
            j -= 1
        array[i] = temp
    
    return array
    