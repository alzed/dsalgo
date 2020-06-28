class PriorityQueue:
    def __init__(self):
        self._array = [0]
        self.length = 1

    @property
    def queue(self):
        return self._array[1:]

    def enqueue(self, element):
        self._array.append(-1)
        self.increase(self.length-1, element)
        self.length += 1

    def dequeue(self):
        if len(self._array) < 2:
            return None
        else:
            self._array[0] = self._array[1]
            self._array[1] = self._array.pop()
            self.length -= 1
            self._max_heapify(1)
            return self._array[0]

    def increase(self, pos, val):
        pos += 1
        if val < self._array[pos]:
            print('Cannot decrement value')
        else:
            self._array[pos] = val
            while pos > 1 and self._array[pos] > self._array[pos//2]:
                self._array[pos], self._array[pos//2] = self._array[pos//2], self._array[pos]
                pos //= 2

    def first(self):
        return self._array[1]
        
    def _max_heapify(self, pos):
        left = 2*pos
        right = 2*pos + 1
        largest = pos
        if left < self.length and self._array[left] > self._array[largest]:
            largest = left
        if right < self.length and self._array[right] > self._array[largest]:
            largest = right
        if not largest == pos:
            self._array[pos], self._array[largest] = self._array[largest], self._array[pos]
            self._max_heapify(largest)
    