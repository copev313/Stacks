#Stacks Project
#Completed as part of Codecademy- Stacks Exercise
#E.Cope (Jan. 2020)

from node import Node

class Stack:
  def __init__(self, limit = 1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  def push(self, value):
    if self.has_space():
      
    	item = Node(value)
    	item.set_next_node(self.top_item)
    	self.top_item = item
    # Increment stack size by 1 here:
    	self.size += 1
    else:
      print("Stack is full!")
        

  def pop(self):
    if (not self.is_empty()):
      item_to_remove = self.top_item
      self.top_item = item_to_remove.get_next_node()
      self.size -= 1
      return item_to_remove.get_value()
    else:
      print("The stack is empty.")
  
  def peek(self):
    if not self.is_empty():
	    return self.top_item.get_value()
    else:
      print("Nothing to see!")
      
  # Define has_space() and is_empty() below:
  def has_space(self):
    return self.limit > self.size
  
  def is_empty(self):
    return self.size == 0 
