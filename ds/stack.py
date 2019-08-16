class Stack:
    'Stack class'
    def __init__(self):
        self._stack = []
        self._length = 0
    
    def to_array(self):
        return list(self._stack[::-1])

    def push(self, item):
        self._stack.append(item)
        self._length += 1

    def pop(self):
        self._length -= 1
        return self._stack.pop()

    def __len__(self):
        return self._length
    
    def top(self):
        return self._stack[-1]
    
    def is_empty(self):
        return not self._length