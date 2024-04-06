import sys
sys.path.append('../../stack')

from stack import init as stackInit

class Node:
  def __init__(self, data: int) -> None:
    self.data = data
    self.next = None

class Queue:
  def __init__(self) -> None:
    self.head = None

  def is_empty(self):
    if self.head == None:
        return True
    else:
        return False
    
  def push(self,data):
    new_node = Node(data)

    if self.head == None:
      self.head = new_node
      return
    
    current = self.head

    while current.next:
      current = current.next
    current.next = new_node

  def pop(self):
    if self.is_empty():
      return None

    popped_node = self.head
    self.head = self.head.next
    popped_node.next = None

    return popped_node.data
  
  def peek(self):
    if self.is_empty():
      return None

    return self.head.data
  
  def revert(self):
    if self.is_empty():
      return None
    
    stack = stackInit(0)
    current = self.head

    while current:
      stack.push(current.data)
      current = current.next

    return stack

  def display(self):
    current = self.head
    while current:
      print(current.data, end=' ')
      current = current.next

  def get_len(self) -> int:
    count = 0
    current = self.head
    while current:
      count += 1
      current = current.next
    return count

def init(len: int):
  q = Queue()

  for i in range(0, len):
    q.push(i + 1)

  return q
