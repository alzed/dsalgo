class Node:
    def __init__(self, data, nextp):
        self.data = data
        self.next = nextp

class Linkedlist:
    def __init__(self):
        self._head = None
        self._tail = self._head
        self._size = 0
    
    def to_array(self):
        array = []
        node = self._head
        while node:
            array.append(node.data)
            node = node.next
        return array

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

    def __setitem__(self, index, item):
        index = self._size - index if index < 0 else index
        if (0 < index >= self._size):
            raise IndexError('Linkedlist index out of range')
        node = self._head
        i = 0
        while node and i < index:
            node = node.next
            i += 1
        node.data = item
        self._size += 1

    def __getitem__(self, index):
        return (self.to_array())[index]

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
        self._size -= 1
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

class DNode:
    def __init__(self, data, prev, nextp):
        self.data = data
        self.prev = prev
        self.next = nextp
        
class DoublyLinkedlist:
    def __init__(self):
        self._header = DNode(None, None, None)
        self._trailer = DNode(None, self._header, None)
        self._header.next = self._trailer
        self._size = 0

    def prepend(self, item):
        self._header.next = DNode(item, self._header, self._header.next)
        self._size += 1

    def append(self, item):
        pre = self._trailer.prev
        suc = self._trailer
        new = DNode(item, pre, suc)
        suc.prev = new
        pre.next = new 
        self._size += 1
    
    def to_array(self):
        array = []
        node = self._header.next
        while node != self._trailer:
            array.append(node.data)
            node = node.next
        return array

    def pop(self):
        pass

    def shift(self):
        pass

    def __len__(self):
        return self._size

    def is_empty(self):
        return not self._size
