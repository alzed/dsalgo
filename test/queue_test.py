import unittest
from ds.queue import Queue

class QueueTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_queue = Queue()

    def test_enque(self):
        self.test_queue.enque(4)
        self.test_queue.enque(5)
        
        self.assertEqual(self.test_queue.to_array(), [4, 5])
   
    def test_deque(self):
        self.test_queue.enque(4)
        self.test_queue.enque(5)

        self.assertEqual(self.test_queue.deque(), 4)
        self.assertEqual(self.test_queue.to_array(), [5])