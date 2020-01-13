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

    def to_array(self):
        array = []
        node = self._header.next
        while node != self._trailer:
            array.append(node.data)
            node = node.next
        return array

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
    
    def __setitem__(self, index, item):
        index = self._size - index if index < 0 else index
        if (0 < index >= self._size):
            raise IndexError('Linkedlist index out of range')
        node = self._header.next
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
        node = self._header.next
        i = 0
        while i < index-1:
            node = node.next
            i += 1
        node.next = DNode(item, node, node.next)
        self._size += 1

    def pop(self):
        if not self._size:
            raise IndexError('Cannot pop from empty list')
        data = self._trailer.prev
        data.prev.next = self._trailer
        self._trailer.prev = data.prev
        self._size -= 1
        return data.data

    def shift(self):
        if not self._size:
            raise IndexError('Cannot shift from empty list')
        data = self._header.next
        self._header.next = data.next
        data.prev = self._header
        self._size -= 1
        return data.data

    def __len__(self):
        return self._size

    def is_empty(self):
        return not self._size
