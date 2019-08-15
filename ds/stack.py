class Stack:
    'Stack class'
    def __init__(self):
        self.stack = []
    
    def to_array(self):
        return list(self.stack[::-1])

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def __len__(self):
        return len(self.stack)
    
    def top(self):
        return self.stack[-1]
    
    def is_empty(self):
        return not(self.stack)