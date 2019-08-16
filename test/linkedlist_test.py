import unittest
from ds.linkedlist import Linkedlist

class LinkedlistTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_linkedlist = Linkedlist()

    def test_to_array(self):
        self.test_linkedlist.prepend(4)
        self.test_linkedlist.prepend(5)

        self.assertEqual(self.test_linkedlist.to_array(), [5, 4])

    def test_append(self):
        self.test_linkedlist.append(4)
        self.test_linkedlist.append(5)
        
        self.assertEqual(self.test_linkedlist.to_array(), [4, 5])
   
    def test_prepend(self):
        self.test_linkedlist.prepend(4)
        self.test_linkedlist.prepend(5)
        
        self.assertEqual(self.test_linkedlist.to_array(), [5, 4])

    def test_pop(self):
        self.test_linkedlist.append(4)
        self.test_linkedlist.append(5)

        self.assertEqual(self.test_linkedlist.pop(), 5)
        self.assertEqual(self.test_linkedlist.to_array(), [4])

    def test_shift(self):
        self.test_linkedlist.append(4)
        self.test_linkedlist.append(5)

        self.assertEqual(self.test_linkedlist.shift(), 4)
        self.assertEqual(self.test_linkedlist.to_array(), [5])

    def test_length(self):
        self.test_linkedlist.append(4)
        self.test_linkedlist.prepend(5)
        self.test_linkedlist.append(4)
        self.test_linkedlist.prepend(5)

        self.assertEqual(len(self.test_linkedlist), 4)