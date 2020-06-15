# Shell sort algorithm

def shell_sort(array):
    arr = array.copy()
    sub_arr_len = len(array)//2

    while sub_arr_len > 0:
        for i in range(sub_arr_len):
            gap_insertion_sort(arr, i, sub_arr_len)
            print(i, arr)
        sub_arr_len //= 2

    return arr

def gap_insertion_sort(array, start, gap):
    arr_len = len(array)
    for i in range(start+gap, arr_len, gap):
        temp = array[i]
        j = i-gap
        while j >= 0:
            if array[j] > temp:
                array[i] = array[j]
                i -= gap
            j -= gap
        array[i] = temp
    