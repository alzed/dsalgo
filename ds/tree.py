class BinaryNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)
        
class BST:
    def __init__(self):
        self._root = None

    def insert(self, item):
        if self._root:
            self._root = self._insert(item, self._root)
        else:
            self._root = BinaryNode(item)

    def _insert(self, item, node):
        if not node:
            return BinaryNode(item)
        elif item < node.data:
            node.left = self._insert(item, node.left)
        elif item > node.data:
            node.right = self._insert(item, node.right)
        return node

    def get_root(self):
        return self._root.data

    def min(self):
        node = self._root
        while node.left:
            node = node.left
        return node.data
    
    def max(self):
        node = self._root
        while node.right:
            node = node.right
        return node.data

    def to_array(self, key='inorder'):
        arr = []
        if key == 'preorder':
            return self._preorder(self._root, arr)
        elif key == 'postorder':
            return self._postorder(self._root, arr)
        return self._inorder(self._root, arr)

    def _preorder(self, node, array):
        if not node:
            return array
        array.append(node.data)
        self._preorder(node.left, array)
        self._preorder(node.right, array)
        return array

    def _inorder(self, node, array):
        if not node: 
            return array
        self._inorder(node.left, array)
        array.append(node.data)
        self._inorder(node.right, array)
        return array

    def _postorder(self, node, array):
        if not node: 
            return array
        self._inorder(node.left, array)
        self._inorder(node.right, array)
        array.append(node.data)
        return array

    def __contains__(self, item):
        return True if self._search(item, self._root) else False

    def _search(self, item, root):
        if not root:
            return False
        if item < root.data:
            root = self._search(item, root.left)
        elif item > root.data:
            root = self._search(item, root.right)
        return root

    def remove(self, item):
        self.delete_node(item, self._root)
        
    def delete_node(self, item, node):
        if not node:
            return node
        elif item < node.data:
            node.left = self.delete_node(item, node.left)
        elif item >  node.data:
            node.right = self.delete_node(item, node.right)
        else:
            if not node.left:
                temp = node.right
                node = None
                return temp

            if not node.right:
                temp = node.left
                node = None 
                return temp

            minimum = self.minimum(node.right)
            node.data = minimum.data
            node.right = self.delete_node(minimum.data, node.right) 
        return node

    def minimum(self, node):
        pre = None
        while node:
            pre = node
            node = node.left
        return pre

    def size(self):
        pass

    def height(self):
        pass

    def is_empty(self):
        return False if self._root else True
