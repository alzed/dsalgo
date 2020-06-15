# Merge sort algorithm

def merge_sort(array):
    arr = array.copy()
    m_sort(arr)
    return arr

def m_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        l_half = arr[:mid]
        r_half = arr[mid:]  
        m_sort(l_half)
        m_sort(r_half)

        i = 0
        j = 0
        k = 0
        
        while i < len(l_half) and j < len(r_half):
            if l_half[i] <= r_half[j]:
                arr[k] = l_half[i]
                i += 1
            else:
                arr[k] = r_half[j]
                j += 1
            k += 1
        
        while i < len(l_half):
            arr[k] = l_half[i]
            i += 1
            k += 1

        while j < len(r_half):
            arr[k] = r_half[j]
            j += 1
            k += 1
