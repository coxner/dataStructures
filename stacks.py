from node import Node

#initializes the stack class
class Stack:
  def __init__(self, limit=1000):
    self.top_item = None
    self.size = 0
    self.limit = limit
  
  #push adds to the top of the stack
  def push(self, value):
    #checks to make sure there is space in the stack
    if self.has_space():
      item = Node(value)
      #sets next node to current top_item
      item.set_next_node(self.top_item)
      #assigns top_item to our newly created node
      self.top_item = item
      #increases the stack size incase there is a size limit set
      self.size += 1
      print("Adding {} to the pizza stack!".format(value))
    else:
      print("No room for {}!".format(value))
  #pop removes data from the top of the stack
  def pop(self):
    #runs as long as stack is not empty
    if not self.is_empty():
      #sets item to remove as the top_item  
      item_to_remove = self.top_item
      #sets top_item to the node after the node we are removing
      self.top_item = item_to_remove.get_next_node()
      #decreases the size of the stack
      self.size -= 1
      print("Delivering " + item_to_remove.get_value())
      return item_to_remove.get_value()
    print("All out of pizza.")

  #peek used to view data of top stack without removing it  
  def peek(self):
    #as long as stack is not empty
    if not self.is_empty():
      #return the value of the top stack  
      return self.top_item.get_value()
    print("Nothing to see here!")

  #method to check if there is space in the stack  
  def has_space(self):
    #as long as stack limit we set is less then the stack size prevents overflow
    return self.limit > self.size
  #checks if the stack is empty prevents underflow  
  def is_empty(self):
    #used as a check condition in other methods
    return self.size == 0

#Code demonstrates the stacks in use  
# Defining an empty pizza stack
pizza_stack = Stack(6)
# Adding pizzas as they are ready until we have 
pizza_stack.push("pizza #1")
pizza_stack.push("pizza #2")
pizza_stack.push("pizza #3")
pizza_stack.push("pizza #4")
pizza_stack.push("pizza #5")
pizza_stack.push("pizza #6")


pizza_stack.push("pizza #7")


print("The first pizza to deliver is " + pizza_stack.peek())
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()
pizza_stack.pop()