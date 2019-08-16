class Deque:
    'Deque class'
    def __init__(self):
        self._deque = []
        self._length = 0
    
    def to_array(self):
        return list(self._deque)

    def enque(self, item):
        self._deque.append(item)
        self._length += 1

    def enque_left(self, item):
        self._deque.insert(0, item)
        self._length += 1
    
    def deque(self):
        self._length -= 1
        return self._deque.pop(0)

    def deque_right(self):
        self._length -= 1
        return self._deque.pop()

    def __len__(self):
        return self._length
    
    def first(self):
        return self._deque[0]

    def last(self):
        return self._deque[-1]
    
    def is_empty(self):
        return not self._length