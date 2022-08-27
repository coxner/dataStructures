class Node:
  def __init__(self, value, next_node=None, prev_node=None):
    self.value = value
    self.next_node = next_node
    self.prev_node = prev_node
    
  def set_next_node(self, next_node):
    self.next_node = next_node
    
  def get_next_node(self):
    return self.next_node

  def set_prev_node(self, prev_node):
    self.prev_node = prev_node
    
  def get_prev_node(self):
    return self.prev_node
  
  def get_value(self):
    return self.value
  

class DoublyLinkedList:
  def __init__(self):
    self.head_node = None
    self.tail_node = None

  #add to the head of a list  
  def add_to_head(self, new_value):
    new_head = Node(new_value)
    current_head = self.head_node
    #checks if there is a current head
    if current_head != None:
      current_head.set_prev_node(new_head)
      new_head.set_next_node(current_head)
    #assigns headnode to the new head node we created  
    self.head_node = new_head
    #checks to make sure that there is a tail if not then the head is both the head node and tail node
    if self.tail_node == None:
      self.tail_node = new_head

    #add to the tail of a node list
  def add_to_tail(self, new_value):
    new_tail = Node(new_value)
    current_tail = self.tail_node

    if current_tail != None:
      current_tail.set_next_node(new_tail)
      new_tail.set_prev_node(current_tail)
    self.tail_node = new_tail

    if self.head_node == None:
      self.head_node = new_tail
    
    #remove the head node from a list
  def remove_head(self):
    removed_head = self.head_node
    if removed_head == None:
      return None
     #assigns head node to the node after the head node we are removing
    self.head_node = removed_head.get_next_node()
    #if our new head nodes previous value is not equal to None we assign it a prev_node = None
    if self.head_node != None:
      self.head_node.set_prev_node(None)
    if self.tail_node == removed_head:
      self.remove_tail()
    return removed_head.get_value()
  #method to remove the tail of the list
  def remove_tail(self):
    removed_tail = self.tail_node
    if removed_tail == None :
      return None
    self.tail_node = removed_tail.get_prev_node()
    if self.tail_node != None:
      self.tail_node.set_next_node(None)
    if removed_tail == self.head_node:
      self.remove_head()
    return removed_tail.get_value()

  #remove a node by its value
  def remove_by_value(self, value_to_remove):
      #by deafault set node to remove to none
      node_to_remove = None
      #set current_node to the head node
      current_node = self.head_node
      #while current node isnt = to none
      while current_node != None:
        if current_node.get_value() == value_to_remove:
          node_to_remove = current_node
          break
        current_node = current_node.get_next_node()
      if node_to_remove == None:
        return None
      #if the node to remove is the head node  
      elif node_to_remove == self.head_node:
        self.remove_head()
      #if the node to remove is the tail node  
      elif node_to_remove == self.tail_node :
        self.remove_tail()
      #else remove the node from in the list and reset the pointer of the nodes surrounding it  
      else :
        next_node = node_to_remove.get_next_node()
        prev_node = node_to_remove.get_prev_node()
        next_node.set_prev_node(prev_node)
        prev_node.set_next_node(next_node)
      return node_to_remove
  #method to turn node list into strings for output  
  def stringify_list(self):
      string_list = ""
      #starts with the head node
      current_node = self.head_node
      while current_node:
        #checks current nodes value is not equal to none
        if current_node.get_value() != None:
            #adds node to the string list then inserts new line
          string_list += str(current_node.get_value()) + "\n"
        #sets the current node to the node following the current node  
        current_node = current_node.get_next_node()
      #returns string_list  
      return string_list

# Create your subway line here:
subway = DoublyLinkedList()
subway.add_to_head("Times Square")
subway.add_to_head("Grand Central")
subway.add_to_head("Central Park")
subway.add_to_tail("Penn Station")
subway.add_to_tail("Wall Street")
subway.add_to_tail("Brooklyn Bridge")
subway.remove_head()
subway.remove_tail()
subway.remove_by_value("Times Square")
print(subway.stringify_list())