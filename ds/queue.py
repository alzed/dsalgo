class Queue:
    'Queue class'
    def __init__(self):
        self.queue = []
    
    def to_array(self):
        return list(self.queue)

    def enque(self, value):
        self.queue.append(value)

    def deque(self):
        return self.queue.pop(0)

    def __len__(self):
        return len(self.queue)
    
    def first(self):
        return self.queue[0]

    def last(self):
        return self.queue[-1]
    
