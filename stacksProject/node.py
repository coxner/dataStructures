# We'll be using our Node class
#Creation of the Node class
class Node:
  def __init__(self, value, next_node=None):
    self.value = value
    self.next_node = next_node
    
  def get_value(self):
    return self.value
  
  def get_next_node(self):
    return self.next_node
  
  def set_next_node(self, next_node):
    self.next_node = next_node

# Our LinkedList class
class LinkedList:
  def __init__(self, value=None):
    self.head_node = Node(value)
  
  def get_head_node(self):
    return self.head_node
  
# Add your insert_beginning and stringify_list methods below:
# Adds nodes to the beginning of the Node list
  def insert_beginning(self, new_value):
    new_node = Node(new_value)
    new_node.set_next_node(self.head_node)
    self.head_node = new_node
    
  def stringify_list(self):
    #collect node values
    string_list = ""
    #sets current node to the head of the node
    current_node = self.get_head_node()
    #while loop to loop through nodes as long as node value is != Null
    while current_node:
      if current_node.get_value() != None:
        string_list += str(current_node.get_value()) + "\n"
        #sets current node to the next node in line
      current_node = current_node.get_next_node()
    return string_list
  
# Define your remove_node method below:
  def remove_node(self, value_to_remove):
    #sets current node to the head node
    current_node = self.get_head_node()
    #if the value of current node which is the head node = value to remove
    if current_node.get_value() == value_to_remove:
      # the head node becomes the second node in the linked list
      self.head_node = current_node.get_next_node()
    else : 
     #While loop to check current nodes value
      while current_node:
        #sets the next nodes value to the node after current node
        next_node = current_node.get_next_node()
        # if the next nodes value is == to value to remove
        if next_node.get_value() == value_to_remove:
          # sets the node linking to current node to the next node   
          current_node.set_next_node(next_node.get_next_node())
          # condition to exit the loop
          current_node = None
        else:
           # continueing checking the loop 
          current_node = next_node