ternary_search = lambda a, e: ternary(a, 0, len(a)-1, e) 

def ternary(array, start, end, element):
    if start < end:
        mid1 = start + (end-start)//3
        mid2 = end - (end-start)//3
        
        if array[mid1] == element:
            return mid1
        if array[mid2] == element:
            return mid2
        
        if element < array[mid1]:
            return ternary(array, start, mid1, element)
        elif element > array[mid2]:
            return ternary(array, mid2, end, element)
        else:
            return ternary(array, mid1, mid2, element)

    return None
