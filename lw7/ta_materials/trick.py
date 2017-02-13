# Here is the binary tree node class that we will use
# Note that the constructor allows us to set the item
# at the node and also its left and right subtrees

class BTNode:
  """A node in a binary tree."""

  def __init__(self: 'BTNode', item: object, 
               left: 'BTNode' =None, right: 'BTNode' =None) -> None:
    """Initialize this node.
    """
    self.item, self.left, self.right = item, left, right

  def __repr__(self):
    return 'BTNode({}, {}, {})'.format(self.item, str(self.left), str(self.right))


def tree_sum(t: BTNode) -> int:
  '''Return the sum of the leaves in t.
  
  >>> t = BTNode(None, BTNode(8), BTNode(9))
  >>> tree_sum(t)
  17
  '''
  if not t:
    return 0
  if not t.left and not t.right:
    return t.item
  return tree_sum(t.left) + tree_sum(t.right)

def tree_height(t: BTNode) -> int:
  '''Return the height of t
  
  >>> tree_height(BTNode(None, BTNode(None, BTNode(4), BTNode(10)), BTNode(9)))
  2
  '''
  if not t:
    return 0
  if not t.left and not t.right:
    return 0
  return 1 + max(tree_height(t.left), tree_height(t.right))

def tree_paths(t: BTNode) -> int:
  '''Return number of paths to get from root of t,
  to all houses, and back to t.
  
  >>> tree_paths(BTNode(None, BTNode(4), BTNode(5)))
  4
  '''
  if not t:
    return 0
  if not t.left and not t.right:
    return 0
  paths1 = tree_paths(t.left)
  paths2 = tree_paths(t.right)
  paths = paths1 + paths2
  paths = paths + 4 # 2 for left, 2 for right
  return paths

def solve(t: BTNode) -> (int, int):
  '''Return the solution to the tree as a tuple of (paths, candy)
  
  >>> solve(BTNode(None, BTNode(5), BTNode(6)))
  (3, 11)
    '''
  candy = tree_sum(t)
  paths = tree_paths(t)
  height = tree_height(t)
  paths = paths - height
  return paths, candy
  
def read_bt(s: str) -> BTNode:
  '''s is a line that represents a binary tree.
  Return the BTNode corresponding to that string.
  >>> read_bt('4')
  BTNode(4, None, None)
  >>> read_bt('(3 4)')
  BTNode(None, BTNode(3, None, None), BTNode(4, None, None))
  >>> read_bt('((1 2) (3 4))')
  BTNode(None, BTNode(None, BTNode(1, None, None), BTNode(2, None, None)), BTNode(None, BTNode(3, None, None), BTNode(4, None, None)))
  
  '''
  return read_bt_helper(s)[0]

def read_bt_helper(s: str) -> (BTNode, str):
  s = s.strip()
  if s[0] == '(':
    left, s = read_bt_helper(s[1:])
    s = s.strip()
    right, s = read_bt_helper(s)
    s = s.strip()
    assert s[0] == ')', 'expected )'
    return BTNode(None, left, right), s[1:]
  else: # must be a digit
    assert s[0].isdigit(), 'digit expected'
    i = 0
    while i < len(s) and s[i].isdigit():
      i = i + 1
    return BTNode(int(s[:i])), s[i:]
  
def process(f) -> None:
  '''
  Solve the problem for all lines in file f.
  '''
  for line in f:
    paths, sum = solve(read_bt(line))
    print(paths, sum)

if __name__ == '__main__':
  import doctest
  doctest.testmod()
  process(open('candy.txt'))
  