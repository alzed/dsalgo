import unittest
from ds.deque import Deque

class DequeTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_deque = Deque()

    def test_to_array(self):
        self.test_deque.enque('4')
        self.test_deque.enque('5')

        self.assertEqual(self.test_deque.to_array(), ['4', '5'])

    def test_enque(self):
        self.test_deque.enque(4)
        self.test_deque.enque(5)
        
        self.assertEqual(self.test_deque.to_array(), [4, 5])
   
    def test_enque_left(self):
        self.test_deque.enque(4)
        self.test_deque.enque_left(5)
        
        self.assertEqual(self.test_deque.to_array(), [5, 4])
   
    def test_dequeue(self):
        self.test_deque.enque(4)
        self.test_deque.enque(5)

        self.assertEqual(self.test_deque.deque(), 4)
        self.assertEqual(self.test_deque.to_array(), [5])

    def test_dequeue_right(self):
        self.test_deque.enque(4)
        self.test_deque.enque(5)

        self.assertEqual(self.test_deque.deque_right(), 5)
        self.assertEqual(self.test_deque.to_array(), [4])

    def test_length(self):
        self.test_deque.enque(4)
        self.test_deque.enque(5)
        self.test_deque.enque(4)
        self.test_deque.deque()

        self.assertEqual(len(self.test_deque), 2)

    def test_first(self):
        self.test_deque.enque(4)
        self.test_deque.enque(5)
        self.test_deque.enque(3)

        self.assertEqual(self.test_deque.first(), 4)

    def test_last(self):
        self.test_deque.enque(4)
        self.test_deque.enque(5)
        self.test_deque.enque(3)

        self.assertEqual(self.test_deque.last(), 3)

    def test_is_empty(self):
        self.assertEqual(self.test_deque.is_empty(), True)