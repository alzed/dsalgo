import unittest
from ds.stack import Stack

class StackTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_stack = Stack()

    def test_to_array(self):
        self.test_stack.push('4')
        self.test_stack.push('5')

        self.assertEqual(self.test_stack.to_array(), ['5', '4'])

    def test_push(self):
        self.test_stack.push(4)
        self.test_stack.push(5)
        
        self.assertEqual(self.test_stack.to_array(), [5, 4])
   
    def test_pop(self):
        self.test_stack.push(4)
        self.test_stack.push(5)

        self.assertEqual(self.test_stack.pop(), 5)
        self.assertEqual(self.test_stack.to_array(), [4])

    def test_length(self):
        self.test_stack.push(4)
        self.test_stack.push(5)
        self.test_stack.push(4)
        self.test_stack.pop()

        self.assertEqual(len(self.test_stack), 2)

    def test_peek(self):
        self.test_stack.push(4)
        self.test_stack.push(5)
        self.test_stack.push(3)

        self.assertEqual(self.test_stack.peek(), 3)

    def test_is_empty(self):
        self.assertEqual(self.test_stack.is_empty(), True)
