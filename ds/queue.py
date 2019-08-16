class Queue:
    'Queue class'
    def __init__(self):
        self._queue = []
        self._length = 0
    
    def to_array(self):
        return list(self._queue)

    def enque(self, item):
        self._queue.append(item)
        self._length += 1

    def deque(self):
        self._length -= 1
        return self._queue.pop(0)

    def __len__(self):
        return self._length
    
    def first(self):
        return self._queue[0]

    def last(self):
        return self._queue[-1]
    
    def is_empty(self):
        return not self._length