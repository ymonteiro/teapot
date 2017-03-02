"""Incomplete Binary Search Tree implementation.
Author: Francois Pitt, March 2013.
        Danny Heap, March 2014
        Dan Zingaro, March 2016
"""

class BST:
    """A Binary Search Tree."""

    def __init__(self, container=[]):
        """(BST, list) -> NoneType
        Initialize this BST by inserting the items from container (default [])
        one by one, in the order given.
        """
        # Initialize empty tree.
        self.root = None
        # Insert every item from container.
        for item in container:
            self.insert(item)

    def __str__(self):
        """(BST) -> str
        Return a "sideways" representation of the values in this BST, with
        right subtrees above nodes above left subtrees and each value preceded
        by a number of TAB characters equal to its depth.
        """
        # helper to recursively represent tree rooted at root as a string
        def _str(indent: str, root: _BSTNode) -> str:
            """
            Return a 'sideways' representation of the values in the BST rooted
            at root, with right subtree indented above root, and left indented
            below root, each value preceded by TAB characters equal to its depth
            """
            if root:
                return (_str(indent + "\t", root.right) +
                        indent + str(root.item) + "\n" +
                        _str(indent + "\t", root.left))
            else:
                return ""
	
        return _str("", self.root)

    def insert(self, item):
        """(BST, object) -> NoneType
        Insert item into this BST.
        """
        # helper function to recursively insert item into tree
        # rooted at root
        def _insert(root: _BSTNode, item: object) -> _BSTNode:
            """Insert value in BST rooted at root, return new root"""
            if not root:
                root = _BSTNode(item)
            elif item < root.item:
                root.left = _insert(root.left, item)
            elif item > root.item:
                root.right = _insert(root.right, item)
            return root
        self.root = _insert(self.root, item)            

    def count_less(self, item):
        """(BST, object) -> int
        Return the number of items in this BST that are strictly less than
        item.
        """
        # ridiculous stub value --- fix this!
        return -42

    def size(self: 'BST') -> int:
        """Return number of nodes in BST self"""
        # helper function
        def _size(root: _BSTNode) -> int:
            """Return number of nodes of BST rooted at root"""
            return _size(root.left) + 1 + _size(root.right) if root else 0
        return _size(self.root)


class _BSTNode:
    """A node in a BST."""

    def __init__(self, item, left=None, right=None):
        """(_BSTNode, object, _BSTNode, _BSTNode) -> NoneType
        Initialize this node to store item and have children left and right.
        """
        self.item, self.left, self.right = item, left, right
