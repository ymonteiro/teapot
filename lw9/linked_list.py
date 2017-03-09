from node import Node

class LinkedListError(Exception):
  pass
  
class LinkedList:

  """Collection of Nodes to form a linked list"""
  
  def __init__(self: 'LinkedList') -> None:
    """Create empty LinkedList"""
    self.front, self.back, self.size = None, None, 0
    
  def __repr__(self: 'LinkedList') -> str:
    """Return str representation of LinkedList"""
    if self.front is None:
      return 'LinkedList()'
    else:
      return repr(self.front)
      
      
  def append(self: 'LinkedList', value: object) -> None:
    """Append Node with value to the end of self."""
    new_node = Node(value)
    if self.size == 0:
      self.front = self.back = new_node
    else:
      self.back.next = new_node
      self.back = new_node
    self.size = self.size + 1
      
  def prepend(self: 'LinkedList', value: object) -> None:
    """Prepend Node with value to the beginning of self."""
    new_node = Node(value)
    if self.size == 0:
      self.front = self.back = new_node
      self.size = 1
    else:
      new_node.next = self.front
      self.front = new_node
      self.size = self.size + 1
      

  def delete_front(self: 'LinkedList') -> None:
    """Delete first node of self."""
    if self.front is None:
      raise LinkedListError('cannot remove from empty list')
    if self.front == self.back:
      self.back = None
    self.front = self.front.next
    self.size = self.size - 1
    
  def __getitem__(self: 'LinkedList', index: int) -> object:
    """Return value at element index of self."""
    if index >= self.size or index < 0:
      raise IndexError('invalid index')
    current_node = self.front
    for step in range(index):
      current_node = current_node.next
    return current_node.value
    
