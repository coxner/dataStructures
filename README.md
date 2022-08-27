# dataStructures

###Nodes

Nodes can be viewed as the base class data structures are built on which varies for each individual data structure. 

**__init__** Pythons equivalant to a constructor in OOP. Called every time object from class created. Initializes objects attributes only purpose it serves.

Can view a basic node working class [here](https://github.com/coxner/dataStructures/blob/master/Queue%20Shell/node.py). Nodes are initialized with two variables, value and next_node. **Value** is just the value given to each node. **next_node** is a pointer that points to the next node.  

**Self** represents class instance. By using it we assign arguments given to the object to the attribute of the class.

**IMPORTANT NOTE** to "delete" a node we re assign the head node which removes the node from the sequence. When a node is reassign the memory space is cleared. 

**set_next_node()** used to set the next node in a data structure. When we start looking at other data structures in depth we will see this function called. 

**get_next_node()** used to get the node next after the current node. Will see this as well used in other data structures. Good example is used to re assign a current node variable before. 

**get_value()** is used to return the value of the node.


