"""Sample solution for Lab 9.
Author: Francois Pitt, March 2013,
        Danny Heap, November 2013.
                    March 2014
"""

from inorder import BTNode, LLNode


def longest(root: BTNode) -> LLNode:
    """Return the first node in a linked list that contains every value on a
    longest path from root to a leaf of the binary tree rooted at root.

    >>> b = BTNode(5)
    >>> str(longest(b))
    '5'
    >>> # from the handout...
    >>> left = BTNode('B', None, BTNode('D', BTNode('G')))
    >>> right = BTNode('C', BTNode('E'), BTNode('F'))
    >>> root = BTNode('A', left, right)
    >>> str(longest(root))
    'A -> B -> D -> G'
    """
    return _longest(root)[1]


def _longest(root: BTNode) -> (int, LLNode):
    """Return the first node in a linked list that contains every value on a
    longest path from root to a leaf of the binary tree rooted at root,
    together with the length of the path.
    """
    if root:
        left = _longest(root.left)
        right = _longest(root.right)
        if left[0] > right[0]:
            return (left[0] + 1, LLNode(root.item, left[1]))
        else:
            return (right[0] + 1, LLNode(root.item, right[1]))
    else: # return 0 is also OK (length of list matters, not height)
        return -1, None # empty tree has height one less than a leaf...


# Test it out on the tree from the handout.
if __name__ == '__main__':
    import doctest
    doctest.testmod()
