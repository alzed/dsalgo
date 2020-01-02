import unittest
from ds.doubly_linkedlist import DoublyLinkedlist

class DoublyLinkedlistTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_doubly_linkedlist = DoublyLinkedlist()

    def test_to_array(self):
        self.test_doubly_linkedlist.prepend(4)
        self.test_doubly_linkedlist.prepend(5)

        self.assertEqual(self.test_doubly_linkedlist.to_array(), [5, 4])

    def test_append(self):
        self.test_doubly_linkedlist.append(4)
        self.test_doubly_linkedlist.append(5)
        
        self.assertEqual(self.test_doubly_linkedlist.to_array(), [4, 5])
   
    def test_prepend(self):
        self.test_doubly_linkedlist.prepend(4)
        self.test_doubly_linkedlist.prepend(5)
        
        self.assertEqual(self.test_doubly_linkedlist.to_array(), [5, 4])

    def test_set(self):
        self.test_doubly_linkedlist.append(4)
        self.test_doubly_linkedlist.append(5)
        self.test_doubly_linkedlist[1] = 6

        self.assertEqual(self.test_doubly_linkedlist.to_array(), [4, 6])

    def test_get(self):
        self.test_doubly_linkedlist.append(4)
        self.test_doubly_linkedlist.append(5)

        self.assertEqual(self.test_doubly_linkedlist[1], 5)

    def test_insert(self):
        self.test_doubly_linkedlist.append(4)
        self.test_doubly_linkedlist.append(5)
        self.test_doubly_linkedlist.append(7)
        self.test_doubly_linkedlist.insert(2, 6)

        self.assertEqual(self.test_doubly_linkedlist.to_array(), [4, 5, 6, 7])

    def test_pop(self):
        self.test_doubly_linkedlist.append(4)
        self.test_doubly_linkedlist.append(5)

        self.assertEqual(self.test_doubly_linkedlist.pop(), 5)
        self.assertEqual(self.test_doubly_linkedlist.to_array(), [4])

    def test_shift(self):
        self.test_doubly_linkedlist.append(4)
        self.test_doubly_linkedlist.append(5)

        self.assertEqual(self.test_doubly_linkedlist.shift(), 4)
        self.assertEqual(self.test_doubly_linkedlist.to_array(), [5])

    def test_length(self):
        self.test_doubly_linkedlist.append(4)
        self.test_doubly_linkedlist.prepend(5)
        self.test_doubly_linkedlist.append(4)
        self.test_doubly_linkedlist.prepend(5)

        self.assertEqual(len(self.test_doubly_linkedlist), 4)   
        