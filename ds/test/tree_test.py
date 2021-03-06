import unittest
from ds.tree import BST

class BSTTest(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_bst = BST()

    def test_to_array(self):
        self.test_bst.insert(5)
        self.test_bst.insert(2)
        self.test_bst.insert(7)

        self.assertEqual(self.test_bst.to_array(), [2, 5, 7])
        self.assertEqual(self.test_bst.to_array(key='preorder'), [5, 2, 7])
        self.assertEqual(self.test_bst.to_array(key='postorder'), [2, 7, 5])
        self.assertEqual(self.test_bst.to_array(key='levelorder'), [5, 2, 7])

    def test_insert(self):
        self.test_bst.insert(5)
        self.test_bst.insert(2)
        self.test_bst.insert(3)

        self.assertEqual(self.test_bst.to_array(), [2, 3, 5])

    def test_remove(self):
        self.test_bst.insert(5)
        self.test_bst.insert(2)
        self.test_bst.insert(3)
        self.test_bst.remove(3)
        
        self.assertEqual(self.test_bst.to_array(), [2, 5])

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
        self.test_bst.insert(7)

        self.assertEqual(self.test_bst.size(), 3)
    
    def test_min_height(self):
        self.test_bst.insert(5)
        self.test_bst.insert(2)
        self.test_bst.insert(7)

        self.assertEqual(self.test_bst.min_height(), 1)
    
    def test_max_height(self):
        self.test_bst.insert(5)
        self.test_bst.insert(2)
        self.test_bst.insert(7)
        self.test_bst.insert(1)

        self.assertEqual(self.test_bst.max_height(), 2)
    
    def test_is_empty(self):
        self.assertEqual(self.test_bst.is_empty(), True)
        
        self.test_bst.insert(5)

        self.assertEqual(self.test_bst.is_empty(), False)
    