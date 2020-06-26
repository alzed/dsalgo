# Heap sort algorithm
def heap_sort(array):
    heaped = heap(array)
    heap_size = len(heaped)
    i = 1
    while i < heap_size:
        heaped[i], heaped[heap_size-1] = heaped[heap_size-1], heaped[i]
        heap_size -= 1
        max_heapify(heaped, i, heap_size)
    return(heaped[1:])

def heap(array):
    arr = array.copy()
    arr.insert(0, 0)
    build_heap(arr, len(arr)) 
    return arr

def build_heap(array, length):
    i = int(length/2) + 1
    while i > 0:
        max_heapify(array, i, length)
        i -= 1

def max_heapify(array, pos, length):
    left = 2*pos
    right = 2*pos + 1
    largest = pos
    if left < length and array[left] > array[largest]:
        largest = left
    if right < length and array[right] > array[largest]:
        largest = right
    if not largest == pos:
        array[pos], array[largest] = array[largest], array[pos]
        max_heapify(array, largest, length)
    
def min_heapify(array, pos, length):
    left = 2*pos
    right = 2*pos + 1
    smallest = pos
    if left < length and array[left] < array[smallest]:
        smallest = left
    if right < length and array[right] < array[smallest]:
        smallest = right
    if not smallest == pos:
        array[pos], array[smallest] = array[smallest], array[pos]
        min_heapify(array, smallest, length)


heap_sort([4,3,2,1])