class SLNode:
  # Class to represent a single node in the linked list
  def __init__(self, value):
    self.value = value        # The data stored in the node
    self.next = None          # Pointer to the next node in the list

class SList:
  # Class to represent the linked list itself
  def __init__(self):
    self.head = None          # Pointer to the first node in the list

  # Add a node to the list
  def add_to_front(self, val):
    
    new_node = SLNode(val)                # Create a node
  
    cuurent_head = self.head              # Get the current head

    new_node.next = cuurent_head          # Set the pointer of the new node to the current head

    self.head = new_node                  # Update the head to be the new node

    return self
  
  # Print values function
  def print_values(self):
      
      current = self.head                 # a pointer to the current node (firstly it is the head)
  
      while current is not None:              # Iterating while current is a node and not None
        print(current.value)

        current = current.next            # Update the current to be the next one

      return self
  
  # Add a node to the end
  def add_to_back(self, val):             

    if self.head is None:                 # If the list is empty, add the new node to the front (front and last here are the same)
      self.add_to_front(val)    
      return self

    new_node = SLNode(val)                # Create a node from the passed value
    
    current = self.head                   # a pointer to the current node (firstly it is the head)  
    
    while current.next is not None:       # Iterating while current is a node and not None
      
      current = current.next              # Update the current to be the next one
    
    current.next = new_node               # After iterating over all nodes, add the new node at the end

    return self
  
  # Remove the first node and return its value
  def remove_from_front(self):
    if self.head is None:                 # Check if the list is empty
      return None
    
    removed_value = self.head.value       # Save the value of the node being removed

    self.head = self.head.next             # Move the head pointer to the next node

    return removed_value

  # Remove the last node and return its value
  def remove_from_back(self):
    if self.head is None:                 # Case 1: List is empty
      return None

    if self.head.next is None:            # Case 2: List has only one node
      removed_value = self.head.value
      self.head = None
      return removed_value
    
    current = self.head                   # Case 3: List has multiple nodes
    # Traverse to the second-to-last node
    while(current.next.next is not None):
      current = current.next

    removed_value = current.next.value    # Save the last node's value
    current.next = None                   # Remove the link to the last node

    return removed_value
  
  # Remove the first node with the given value
  def remove_val(self, val):
    if self.head is None:                 # If the list is empty, nothing to remove
      return self
    
    if self.head.value == val:            # If the value is at the head, remove from front
      self.remove_from_front()
      return self

    current = self.head                   # Traverse the list to find the value
    while(current.next is not None):
      if(current.next.value == val):      # If next node has the value, skip it
        current.next = current.next.next
        return self
      current = current.next

    return self
  
  # Insert a node with value 'val' at position 'n'
  def insert_at(self, val, n):
        if n == 0:                        # If index is 0, add to the front
            self.add_to_front(val)
            return self
        
        new_node = SLNode(val)
        current = self.head
        count = 0
        
        # Traverse to the (n-1)th node
        while current is not None and count < n - 1:
            current = current.next
            count += 1
        
        if current is None:               # If index is out of bounds, add to the back
            self.add_to_back(val)
        else:                             # Insert the node between current and current.next
            new_node.next = current.next
            current.next = new_node
            
        return self
    



my_list = SList()                         # create a new instance of a list
my_list.add_to_front("are").add_to_front("Linked lists").add_to_back("fun!").print_values() 
my_list.remove_from_front()
my_list.remove_from_back()
my_list.print_values()


