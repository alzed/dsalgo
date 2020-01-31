# Searching for an element in an array using binary search algorithm
 
def binary_search(array, element):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start+end)//2
        if array[mid] == element:
            return mid
        elif array[mid] > element:
            end = mid-1
        else:
            start = mid+1
    return None
    