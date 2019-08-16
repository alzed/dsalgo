import unittest
from ds.queue import Queue

class QueueTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_queue = Queue()

    def test_to_array(self):
        self.test_queue.enque('4')
        self.test_queue.enque('5')

        self.assertEqual(self.test_queue.to_array(), ['4', '5'])

    def test_enque(self):
        self.test_queue.enque(4)
        self.test_queue.enque(5)
        
        self.assertEqual(self.test_queue.to_array(), [4, 5])
   
    def test_deque(self):
        self.test_queue.enque(4)
        self.test_queue.enque(5)

        self.assertEqual(self.test_queue.deque(), 4)
        self.assertEqual(self.test_queue.to_array(), [5])

    def test_length(self):
        self.test_queue.enque(4)
        self.test_queue.enque(5)
        self.test_queue.enque(4)
        self.test_queue.deque()

        self.assertEqual(len(self.test_queue), 2)

    def test_first(self):
        self.test_queue.enque(4)
        self.test_queue.enque(5)
        self.test_queue.enque(3)

        self.assertEqual(self.test_queue.first(), 4)

    def test_last(self):
        self.test_queue.enque(4)
        self.test_queue.enque(5)
        self.test_queue.enque(3)

        self.assertEqual(self.test_queue.last(), 3)

    def test_is_empty(self):
        self.assertEqual(self.test_queue.is_empty(), True)