class Heap:
    def __init__(self, array):
        self.array = array.copy()
        self.array.insert(0,0)
        self.length = len(self.array)
        self.build_heap(self.array, self.length) 
    
    @property
    def heap(self):
        return self.array

    def build_heap(self, array, length):
        i = int(length/2)
        while i > 0:
            self.min_heapify(array, i, length)
            i -= 1

    def max_heapify(self, array, pos, length):
        left = 2*pos
        right = 2*pos + 1
        largest = pos
        if left < length and array[left] > array[largest]:
            largest = left
        if right < length and array[right] > array[largest]:
            largest = right
        if not largest == pos:
            array[pos], array[largest] = array[largest], array[pos]
            self.max_heapify(array, largest, length)
        
    def min_heapify(self, array, pos, length):
        left = 2*pos
        right = 2*pos + 1
        smallest = pos
        if left < length and array[left] < array[smallest]:
            smallest = left
        if right < length and array[right] < array[smallest]:
            smallest = right
        if not smallest == pos:
            array[pos], array[smallest] = array[smallest], array[pos]
            self.min_heapify(array, smallest, length)
