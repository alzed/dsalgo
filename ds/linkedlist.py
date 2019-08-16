import copy 

class Node:
    def __init__(self, data, nextp):
        self.data = data
        self.next = nextp

class Linkedlist:
    def __init__(self):
        self._head = None
        self._tail = self._head
        self._size = 0

    def prepend(self, item):
        self._head = Node(item, self._head)
        self._size += 1

    def append(self, item):
        new_node = Node(item, None)
        if not self._head: 
            self._head = new_node
        else:
            self._tail.next = new_node
        self._tail = new_node
        self._size += 1

    def to_array(self):
        array = []
        node = self._head
        while node:
            array.append(node.data)
            node = node.next
        return array

    def pop(self):
        if self.is_empty():
            raise IndexError('Cannot pop from empty list')
        current = self._head
        prev = None
        while current.next:
            prev = current
            current = current.next
        value = current.data
        if not prev:
            self._head = None
            self._tail = self._head
        else:
            prev.next = None
            self._tail = prev
        self._size -=1
        return value

    def shift(self):
        if self.is_empty():
            raise IndexError('Cannot pop from empty list')
        head = self._head
        self._head = head.next
        self._size -= 1
        return head.data
        
    def __len__(self):
        return self._size

    def is_empty(self):
        return not self._size

