from copy import deepcopy

def selection_sort(arr):
    array = deepcopy(arr)
    arr_len = len(array)
    for i in range(arr_len):
        minimum = i
        for j in range(i+1, arr_len):
            if array[j] < array[minimum]:
                minimum = j
        array[i], array[minimum] = array[minimum], array[i]
    return array
    