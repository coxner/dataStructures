from node import Node

#initalizes the queue class
class Queue:
  def __init__(self, max_size=None):
    self.head = None
    self.tail = None
    self.max_size = max_size
    self.size = 0
    
  # enqueue adds a item to the queue  
  def enqueue(self, value):
    #checks if there is space in the queue
    if self.has_space():
      item_to_add = Node(value)
      print("Adding " + str(item_to_add.get_value()) + " to the queue!")
      #if the queue is empty assign head and tail to the item we are adding
      if self.is_empty():
        self.head = item_to_add
        self.tail = item_to_add
        #if the queue is not empty we add it at the end 
      else:
        #sets the node of current tail to the node we are adding
        self.tail.set_next_node(item_to_add)
        #sets the tail to node added
        self.tail = item_to_add
      # keeps track of queue size  
      self.size += 1
    else:
      print("Sorry, no more room!")
  
  #dequeue removes an item from the queue       
  def dequeue(self):
    #only can run if queue is not empty
    if self.get_size() > 0:
      #we are removing the head node  
      item_to_remove = self.head
      print(str(item_to_remove.get_value()) + " is served!")
      #if only one item in the queue we remove it and we reasign the head and tail to 0
      if self.get_size() == 1:
        self.head = None
        self.tail = None
      #if there is more then one item in queue we assign the head node to the node after the one we are removing  
      else:
        self.head = self.head.get_next_node()
      #decreases the queue size  
      self.size -= 1
      #returns value of item we are removing
      return item_to_remove.get_value()
    else:
      print("The queue is totally empty!")
  
  #retrives data from front of queue without removing it
  def peek(self):
    #as long as there is item in the queue
    if self.size > 0:
      #return the value of the head  
      return self.head.get_value()
    else:
      print("No orders waiting!")
  
  #gets size of queue
  def get_size(self):
    return self.size
  #check if queue has space
  def has_space(self):
    #if no max size has been set
    if self.max_size == None:
      return True
    #if max size is set we check that our queue size if not bigger then the max size  
    else:
      return self.max_size > self.get_size()
  #checks if queue is empty logic used in other functions  
  def is_empty(self):
    return self.size == 0

#lines of code to demonstrate program
print("Creating a deli line with up to 10 orders...\n------------")
deli_line = Queue(10)
print("Adding orders to our deli line...\n------------")
deli_line.enqueue("egg and cheese on a roll")
deli_line.enqueue("bacon, egg, and cheese on a roll")
deli_line.enqueue("toasted sesame bagel with butter and jelly")
deli_line.enqueue("toasted roll with butter")
deli_line.enqueue("bacon, egg, and cheese on a plain bagel")
deli_line.enqueue("two fried eggs with home fries and ketchup")
deli_line.enqueue("egg and cheese on a roll with jalapeos")
deli_line.enqueue("plain bagel with plain cream cheese")
deli_line.enqueue("blueberry muffin toasted with butter")
deli_line.enqueue("bacon, egg, and cheese on a roll")
deli_line.enqueue("western omelet with home fries")

print("------------\nOur first order will be " + deli_line.peek())
print("------------\nNow serving...\n------------")
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()
deli_line.dequeue()

deli_line.dequeue()
