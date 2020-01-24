# Counting sort algorithm

def counting_sort(array):
    max_value = max(array)+1
    aux_array = [0]*max_value

    for a in array:
        aux_array[a] += 1
    
    sorted_array = [0]*len(array)
    j = 0
    for i, v in enumerate(aux_array):
        while v:
            sorted_array[j] = i
            j += 1
            v -= 1
            
    return sorted_array
