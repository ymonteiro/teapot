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
    
  def delete_return_front(self: 'LinkedList') -> object:
    """Delete first node of self and return value of that node."""
    if self.front is None:
      raise LinkedListError('cannot remove from empty list')
    ret = self.front.value
    if self.front == self.back:
      self.back = None
    self.front = self.front.next
    self.size = self.size - 1
    return ret
    
  def return_front(self: 'LinkedList') -> object:
    """Return value of first node of self."""
    if self.front is None:
      raise LinkedListError('cannot retrieve from empty list')
    return self.front.value

  def is_empty(self: 'LinkedList') -> bool:
    """Return True iff self is empty."""
    return self.front is None
    
  def __len__(self: 'LinkedList') -> int:
    """Return number of items in linked list."""
    return self.size
    
  def __setitem__(self: 'LinkedList', index: int, val: object):
    """Set item at index to val; raise IndexError if ind is invalid."""
    if index >= self.size or index < 0:
      raise IndexError('invalid index')
    current_node = self.front
    for step in range(index):
      current_node = current_node.next
    current_node.value = val
    
  def __contains__(self: 'LinkedList', val: object) -> bool:
    """Return True iff self contains val."""
    # remember the wrapper class where the first node is a Node
    current_node = self.front
    # check through the list to find the value
    while current_node:
      if current_node.value == val:
        # stop and return True
        return True
      current_node = current_node.next
    # reached the end of the list and didn't find it, return False
    return False

  def __delitem__(self: 'LinkedList', index: int) -> object:
    """Remove node at index of self."""
    if index >= self.size or index < 0:
      raise IndexError('invalid index')
    self.size = self.size - 1
    cur = self.front
    # want to stop at the item before the one to delete
    for i in range(index - 1):
      cur = cur.next
    # if you're deleting the first element
    # want to update the front var in wrapper
    if index == 0:
      self.front = self.front.next
    else:
      cur.next = cur.next.next
    # if last element is being deleted, update back
    if not cur.next:
      self.back = cur

  def insert(self: 'LinkedList', index: int, val: int) -> object:
    """Add val at index of self."""
    if index > self.size or index < 0:
      raise IndexError('invalid index')
    self.size = self.size + 1
    cur = self.front
    # go to the index just before
    for i in range(index - 1):
      cur = cur.next
    # if first index, update front
    if index == 0:
      self.front = Node(val, self.front)
    # in the middle somewhere 
    else:
      cur.next = Node(val, cur.next)
    # if the new node added was second to last
    # this means that self.back moved over and now self.back.next exists
    # reset self.back
    if self.back.next:
      self.back = self.back.next

if __name__ == '__main__':
  list1 = LinkedList()  # creates a new empty linked list
  print(len(list1))  # automatically calls list1.__len__(); prints '0'
  print(5 in list1)  # automatically calls list1.__contains__(5); prints 'False'
  try:
    print(list1[0])  # automatically calls list1.__getitem(0); raises IndexError
  except IndexError:
    print('Index error')
  list1.prepend(15)
  list1.prepend(17)
  print(len(list1)) # prints '2'
  print(list1[0]) # prints '17'
  list1[0] = 19 # automatically calls list1.__setitem__(0, 19)
  print(15 in list1) # automatically calls list1._contains(15); prints True
  del list1[1] # automatically calls list1.__delitem__(1)
  print(len(list1)) # prints 1
  list1.prepend(19)
  print(list1)
  list1.insert(1, 23)
  print(list1)
  