from .linkedlist import Linkedlist

class Queue:
    'Queue class'
    def __init__(self, array=None):
        if array:
            self._queue = array
            self._length = len(array)
        else:
            self._queue = []
            self._length = 0
    
    def to_array(self):
        return list(self._queue)

    def enqueue(self, item):
        self._queue.append(item)
        self._length += 1

    def dequeue(self):
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

class QueueList:
    'Queue implemented as a linked list'
    def __init__(self, array = None):
        self._queue = Linkedlist()
        if array:
            for i in array:
                self._queue.append(i)
        self._length = len(self._queue)

    def to_array(self):
        return self._queue.to_array()

    def enqueue(self, item):
        self._queue.append(item)
        self._length += 1

    def dequeue(self):
        self._length -= 1
        return self._queue.shift()

    def __len__(self):
        return self._length
    
    def first(self):
        return self._queue[0]

    def last(self):
        return self._queue[-1]
    
    def is_empty(self):
        return self._queue.is_empty()
        