class BinaryNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

class BST:
    def __init__(self):
        self._root = None
        self._size = 0
        self._min = None
        self._max = None
        
    def to_array(self):
        return self._preorder(self._root, [])

    def insert(self, item):
        self._place(item)
        self._size += 1

    def remove(self, item):
        pass

    def get_root(self):
        pass

    def search(self, item):
        pass

    def min(self):
        pass
    
    def max(self):
        pass

    def size(self):
        return self._size

    def height(self):
        pass

    def is_empty(self):
        return not self._size

    def _place(self, item, node=None):
        root = self._root if not node else node
        if not root: 
            root = BinaryNode(item, None, None)
        elif item < root:
            self._place(item, root.left)
        elif item > root:
            self._place(item, root.right)

    def _preorder(self, node, array):
        if not node:
            return None
        array.append(node.data)
        self._preorder(node.left, array)
        self._preorder(node.right, array)
        return array
