# dataStructures

### Nodes

Nodes can be viewed as the base class data structures are built on which varies for each individual data structure. 

**__init__** Pythons equivalant to a constructor in OOP. Called every time object from class created. Initializes objects attributes only purpose it serves.

Can view a basic node working class [here](https://github.com/coxner/dataStructures/blob/master/Queue%20Shell/node.py). Nodes are initialized with two variables, value and next_node. **Value** is just the value given to each node. **next_node** is a pointer that points to the next node.  

**Self** represents class instance. By using it we assign arguments given to the object to the attribute of the class.

**IMPORTANT NOTE** to "delete" a node we re assign the head node which removes the node from the sequence. When a node is reassign the memory space is cleared. 

**set_next_node()** used to set the next node in a data structure. When we start looking at other data structures in depth we will see this function called. 

**get_next_node()** used to get the node next after the current node. Will see this as well used in other data structures. Good example is used to re assign a current node variable before. 

**get_value()** is used to return the value of the node.

### Linked List

One of the most basic data structures they are a list comprised of nodes. They contain dzta and a pointer to the next node. Head node is first node in data structure and last node is refered to as the tail node. 

The best place to view the code for a linked list is [here](https://github.com/coxner/dataStructures/blob/master/linkedlist.py)

**__init__** initializes the linked list node sets the head node to none to create a empty list.

**get_head_node()** method to return the head node of the data structure. 

**insert_beginning()** First line creates the new node that will be added to the list. Second line sets the pointer for the new head node to the current head node. Final line sets the newly created node as the head node. 

**stringify_list()** method to put the values of notes into a lsit of strings. Syntax straight forward and easy to follow. 

**remove_node()** starts by setting current node variable to the head node. We remove a node in this method by checking its value. If statement used to check if the head node is the node we need to remove. If it is not the while loop runs since we already checked the value of the head node we create a next_node variable and set it to the node following the head node. If statement is then run if the next_node value is equal to the value to remove and the current_node next node is set to the node following the node we are removing. It then sets the current_node to equal None to exit the loop. If the value to remove is not equal to the next node we set the current node to equal the next node and the loop keeps running until the value to remove is found. 

### Doubly Linked List

Doubly linked list is the same as linked list except it contains two pointers one to the next node and one to the previous node. 

**__init__** in the node class initalizes the class with three attributes the value, next_node and prev_node. Only thing thats different from the the linked list data structure is the prev_node attribute.

The remaining methods of the node class are pretty strightforward and understanding can be gathered from reading code. 

Now looking at the DoublyLinkedList class...

**__init__** initalizes the class by setting the list head node and tail node. 

**add_to_head()** is a little different then adding to a linked list because we need to set the current heads prev node to the value we are inserting. Method starts by creating a new node to be the head node and setting the current_head variable to the head node of the list. First if statement checks to make sure there is a head node in the list. If there is we set the current heads prev node to the new node we are adding and set the node we are addings next node to what used to be the head node. Following line assigns the the head node of the list to the node we just created. If statement checks incase item we are adding is the first item in the list if it is, it becomes both the head and tail node for the list.

**add_to_tail()** very similar to the previous method. Follows the exact same logic except it assigns nodes as prev node and not next node. Last if statement checks incase the node we are adding to the tail is the only item in the list. If it is it also becomes the head node. 

**remove_head()** method is a bit different then removing the node from a linked list because we must re assign the value of the prev_node attribute to be none on the node we want to become the head node. Starting lines of method assign the current head node to a variable and checks to make sure there is a head node in the list. Next line sets the head node to the node following the node we want to remove. If statement runs as long as the head nodes new value is not equal to none. If its not it sets the prev node value equal to None because we are removing the head node and there is no link there anymore. If the tail node is also equal to the value we are removing we call the remove tail method as well. 

**remove_tail()** very similar to the **remove_head()** syntax follows the same logic if statement at the end except last if statement calls the remove_head() method if the tail we are removing is also the head_node. 


