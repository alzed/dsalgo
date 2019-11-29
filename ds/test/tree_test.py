import unittest
from ds.tree import BST

class BSTTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_bst = BST()

    def test_to_array(self):
        self.test_bst.insert(5)
        self.test_bst.insert(2)
        self.test_bst.insert(3)

        self.assertEqual(self.test_bst.to_array(), [5, 2, 3])

    def test_insert(self):
        self.test_bst.insert(5)
        self.test_bst.insert(2)
        self.test_bst.insert(3)

        self.assertEqual(self.test_bst.to_array(), [5, 2, 3])

    def test_remove(self):
        self.test_bst.insert(5)
        self.test_bst.insert(2)
        self.test_bst.insert(3)

        self.assertEqual(self.test_bst.remove(3), 3)
        self.assertEqual(self.test_bst.to_array(), [5, 2])

    def test_get_root(self):
        self.test_bst.insert(5)
        self.test_bst.insert(2)
        self.test_bst.insert(3)

        self.assertEqual(self.test_bst.get_root(), 5)

    def test_search(self):
        self.test_bst.insert(5)
        self.test_bst.insert(2)
        self.test_bst.insert(3)

        self.assertEqual(5 in self.test_bst, True)
        self.assertEqual(2 not in self.test_bst, False)
        self.assertEqual(7 not in self.test_bst, True)
    
    def test_min(self):
        self.test_bst.insert(5)
        self.test_bst.insert(2)
        self.test_bst.insert(3)

        self.assertEqual(self.test_bst.min(), 2)

    def test_max(self):
        self.test_bst.insert(5)
        self.test_bst.insert(2)
        self.test_bst.insert(3)

        self.assertEqual(self.test_bst.max(), 5)

    def test_size(self):
        self.test_bst.insert(5)
        self.test_bst.insert(2)
        self.test_bst.insert(3)

        self.assertEqual(self.test_bst.size(), 3)
    
    def test_height(self):
        self.test_bst.insert(5)
        self.test_bst.insert(2)
        self.test_bst.insert(3)

        self.assertEqual(self.test_bst.height(), 2)
    
    def test_is_empty(self):
        self.assertEqual(self.test_bst.is_empty(), True)
        
        self.test_bst.insert(5)

        self.assertEqual(self.test_bst.is_empty(), False)
    