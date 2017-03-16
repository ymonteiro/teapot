"""Sample solution for Lab 8.
Author: Francois Pitt, March 2013,
        Danny Heap, November 2013
                    March 2014
"""


class BTNode:
    """A node in a binary tree."""

    def __init__(self: 'BTNode', item: object, 
                 left: 'BTNode' =None, right: 'BTNode' =None) -> None:
        """Initialize this node.
        """
        self.item, self.left, self.right = item, left, right


class LLNode:
    """A node in a linked list."""

    def __init__(self: 'LLNode', item: object, link: 'LLNode' =None) -> None:
        """Initialize this node.
        """
        self.item, self.link = item, link

    def __str__(self: 'LLNode') -> str:
        """Return an informative string showing self


        >>> b = LLNode(1, LLNode(2, LLNode(3)))
        >>> str(b)
        '1 -> 2 -> 3'
        """
        return str(self.item) + (' -> ' + str(self.link) if self.link else '')

    def __repr__(self: 'LLNode') -> str:
        """Return a string that represents self in constructor (initializer) form.

        >>> b = LLNode(1, LLNode(2, LLNode(3)))
        >>> repr(b)
        'LLNode(1, LLNode(2, LLNode(3)))'
        """
        return ('LLNode({}, {})'.format(repr(self.item), repr(self.link)) 
                if self.link else 'LLNode({})'.format(repr(self.item)))

def inorder(root: BTNode) -> LLNode:
    """Return the first node in a linked list that contains every value from the
    binary tree rooted at root, listed according to an inorder traversal.

    >>> b = BTNode(1, BTNode(2), BTNode(3))
    >>> repr(inorder(b))
    'LLNode(2, LLNode(1, LLNode(3)))'
    >>> b2 = BTNode(4, BTNode(5))
    >>> b3 = BTNode(7, b, b2)
    >>> str(inorder(b3))
    '2 -> 1 -> 3 -> 7 -> 5 -> 4'
    >>> # from the handout...
    >>> left = BTNode('B', None, BTNode('D', BTNode('G')))
    >>> right = BTNode('C', BTNode('E'), BTNode('F'))
    >>> root = BTNode('A', left, right)
    >>> str(inorder(root))
    'B -> G -> D -> A -> E -> C -> F'
    """
    return _inorder(root)[0] # what must this first item represent?


def _inorder(root: BTNode) -> (LLNode, LLNode): # what are these 1st and 2nd things?
    """Return the first and last nodes in a linked list that contains every
    value from the binary tree rooted at root, listed according to an inorder
    traversal.
    """
    #if root:
        #head_left, tail_left = _inorder(root.left)
        #head_right, tail_right = _inorder(root.right)
        #node_root = LLNode(root.item, head_right)
        #if tail_left:
            #tail_left.link = node_root
        #return head_left or node_root, tail_right or node_root
    #else:
        #return None, None
        
    """
    >>> left = BTNode('B', None, BTNode('D', BTNode('G')))
    >>> right = BTNode('C', BTNode('E'), BTNode('F'))
    >>> root = BTNode('A', left, right)
    >>> str(inorder(root))
    'B -> G -> D -> A -> E -> C -> F'
    """    
        
    if not root:
        return None, None
    
    else:
        # Start off by making a new node of our item, with None for a link
        # Obviously we will need to replace that None if we have a right branch
        new_node = LLNode(root.item)
        
        # Recursive call on right branch gives us its head and tail        
        right_head, right_tail = _inorder(root.right)
        
        # The link on our new node should be the right head, even if it's None
        new_node.link = right_head
        
        # Ultimately the tail for this whole node will be the rightmost tail
        # If there is no right side, though, this node is the rightmost tail
        if not right_tail:
            right_tail = new_node
        
        # Recursive call on left branch gives us its head and tail
        left_head, left_tail = _inorder(root.left)
        
        # If there is a left tail, we should string our current node to the end
        if left_tail:
            left_tail.link = new_node
        
        # Ultimately the head for this whole node will be the leftmost head
        # If there is no left head, though, this node is the leftmost head
        if not left_head:
            left_head = new_node
        
        # Return the leftmost head and the rightmost tail
        return left_head, right_tail
            

if __name__ == '__main__':
    import doctest
    doctest.testmod()
