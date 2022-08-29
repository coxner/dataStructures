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

Doubly linked list is the same as linked list except it contains two pointers one to the next node and one to the previous node and it can be viewed [here](https://github.com/coxner/dataStructures/blob/master/doublyLinkedList.py). 

**__init__** in the node class initalizes the class with three attributes the value, next_node and prev_node. Only thing thats different from the the linked list data structure is the prev_node attribute.

The remaining methods of the node class are pretty strightforward and understanding can be gathered from reading code. 

Now looking at the DoublyLinkedList class...

**__init__** initalizes the class by setting the list head node and tail node. 

**add_to_head()** is a little different then adding to a linked list because we need to set the current heads prev node to the value we are inserting. Method starts by creating a new node to be the head node and setting the current_head variable to the head node of the list. First if statement checks to make sure there is a head node in the list. If there is we set the current heads prev node to the new node we are adding and set the node we are addings next node to what used to be the head node. Following line assigns the the head node of the list to the node we just created. If statement checks incase item we are adding is the first item in the list if it is, it becomes both the head and tail node for the list.

**add_to_tail()** very similar to the previous method. Follows the exact same logic except it assigns nodes as prev node and not next node. Last if statement checks incase the node we are adding to the tail is the only item in the list. If it is it also becomes the head node. 

**remove_head()** method is a bit different then removing the node from a linked list because we must re assign the value of the prev_node attribute to be none on the node we want to become the head node. Starting lines of method assign the current head node to a variable and checks to make sure there is a head node in the list. Next line sets the head node to the node following the node we want to remove. If statement runs as long as the head nodes new value is not equal to none. If its not it sets the prev node value equal to None because we are removing the head node and there is no link there anymore. If the tail node is also equal to the value we are removing we call the remove tail method as well. 

**remove_tail()** very similar to the **remove_head()** syntax follows the same logic if statement at the end except last if statement calls the remove_head() method if the tail we are removing is also the head_node. 

**remove_by_value()** more complex method but when broken down code is clear to understand. First two lines assign two variables. While loop runs similar to loops we saw before as long as the current_node is not equal to None. If the current nodes value is the node we want to remove we break from the loop because we have found what we are looking for. current_node is reassigned each time the while loop runs to make sure the valuewe are looking for is found. After the value is found through the while loop a few if statements are executed to keep list structure in tact. First if that runs is to check if the noe_to_remove is equal to None if it is we return None. The two following if statements check if the node to remove is the head or the tail if it is we call those respective methods. The else is called if the node we wish to remove is somewhere within the list. If this is the case we find the node we wish to removes next node and prev node. If this is the case we set the node after the node we wish to removes previous node to the node befpre the node we wish to remove. We also so the prev nodes next node to the node after the node we are removing to ensure the structure of the list stays in tact.

### Queues 

Queues are an ordered data structure that follow the model of First in first out. Think concept that the first person to enter a line is the first one to get served. In a queue only the front and back nodes can be accessed. Code can be viewed [here](https://github.com/coxner/dataStructures/blob/master/Queue%20Shell/queue.py)

The underlying data structure of a queue is a linked list. 

**__init__** initalizes a queue the two values that are different are max_size of the queue which as it states is the max size of nodes queue can hold. The next variable is size which by default we assign to 0 this is the current size of the queue.

We will review all of the queue methods.

**get_size()** is a simple method which returns the size of the queue.

**is_empty()** will return true if size of queue is equal to 0. We will see this method used in other functions in the future is a important function to check if the queue is empty or not.

**has_space()** checks if there is space in the queue to add nodes to. First if statement checks to see if there is a max_size set if theres not it returns true and there will always be space in the queue. Else it checks if the max size is greater then the size of the queue. If it is it returns true and we could add elements to the queue if not it returns false and there is no space left in the queue.

**peek()** is a simple method used to get the value of the head node in the queue.

**enqueue()** adds data to the back of the queue. First if statement checks to make sure there is space in the queue for data to be added. If there is we create a new node to add to the queue. Next if statement checks if the queue is empty if it is we assign the node we are adding as the head and the tail node. If it is not the first element to add we set the current tails next node to the node we are adding. After that we set the tail as the node we are adding and then increase the size of the queue by one.

**dequeue()** does the opposite of enqueue and removes a node from the queue. Remeber we can only remove elements from the head of the queue. We first call get_size() in the if statement to make sure there is a node there to remove. We set the node we want to remove to the head node. After that the if statement checks to see if there is only one linked list in the queue. If there is only one element in the queue and we remove it we must set the values of head and tail to none because the queue will then be empty. If there is more then one element he assign the head node to the next node in the queue. We then make sure to decrease the size of the queue by 1.

### Stacks

Stacks are a last in first out data structure. Data can only be added and removed from the top of the stack. Implemented using a linked list. First element added gets pushed to the bottom of the stack. Code can be viewed [here](https://github.com/coxner/dataStructures/blob/master/stacks.py)

**__init__** initalizes the stack class sets the size of the stack equal to 0. Sets the top_item of the stack equal to None. Sets the limit of linked list elements the stack can hold equal to limit.

**is_empty() has_space() and peek()** all this methods follow the same logic as methods from the queue class understanding of methods can be derived from there.

**push()** adds a item to the top of the stack. Runs an if statement to make sure there is room to add an element. Method first creates a new node and then sets the next node equal to what is now the top_item in the stack. We then assign the top_item of the stack to the node we just created and increase the size of the stack by one.

**pop()** does the opposite of push and removes the top_item from the stack. First checks to make sure the stack is not empty and there is something to remove. We assign a variable to the top_item and then reassign the top_item to the next node. After that we decreases the size of the stack by one since we are removing an item. 

### Hash Maps

Is a key value data structure that uses an array and a hashing function to store and retrieve data. 









