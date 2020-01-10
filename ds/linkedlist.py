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

    def __getitem__(self, index):
        return (self.to_array())[index]

    def insert(self, index, item):
        index = self._size - index if index < 0 else index
        if index not in range(self._size):
            raise IndexError('Linkedlist index out of range')
        node = self._head
        i = 0
        while i < index-1:
            node = node.next
            i += 1
        node.next = Node(item, node.next)
        self._size += 1

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

class SinglyLinkedlist:
    def __init__(self):
        self._head = None
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
            current_node = self._head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node
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

    def __getitem__(self, index):
        return (self.to_array())[index]

    def insert(self, index, item):
        index = self._size - index if index < 0 else index
        if index not in range(self._size):
            raise IndexError('Linkedlist index out of range')
        node = self._head
        i = 0
        while i < index-1:
            node = node.next
            i += 1
        node.next = Node(item, node.next)
        self._size += 1

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
        else:
            prev.next = None
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
