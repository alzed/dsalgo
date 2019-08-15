import unittest
from ds.stack import Stack

class StackTest(unittest.TestCase):

    def __init__(self):
        super().__init__()
        self.test_stack = Stack()

    def test_push(self):
        self.test_stack.push(4)
        self.assertEqual(self.test_stack.to_array(), [4])
   
