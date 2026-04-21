class DLNode:
    """
    A class to represent a node in a doubly linked list.
    Each node stores a value and maintains pointers to both the next and previous nodes.
    """
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """
    A class to represent a doubly linked list.
    Enables bidirectional traversal and efficient node operations.
    """
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, val):
        """Adds a new node to the beginning of the list."""
        new_node = DLNode(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        return self

    def add_to_back(self, val):
        """Adds a new node to the end of the list."""
        new_node = DLNode(val)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        return self

    def insert_at(self, val, index):
        """Inserts a node at a particular index (zero-based)."""
        if index <= 0 or not self.head:
            return self.add_to_front(val)
        
        new_node = DLNode(val)
        # Handle case where index is 0 but list is not empty
        if index == 0:
            return self.add_to_front(val)

        current = self.head
        count = 0
        
        # Traverse to find the insertion point
        while current and count < index:
            current = current.next
            count += 1
            
        if not current: # Index is beyond end of list
            return self.add_to_back(val)
        
        # Insert before 'current'
        new_node.next = current
        new_node.prev = current.prev
        if current.prev:
            current.prev.next = new_node
        else:
            self.head = new_node # We are inserting at the head
            
        current.prev = new_node
            
        return self

    def remove_val(self, val):
        """Deletes the first node found with the given value."""
        current = self.head
        while current:
            if current.value == val:
                # Update pointers to bypass the current node
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next # Node was the head
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev # Node was the tail
                
                return self
            current = current.next
        return self

    def print_values(self):
        """Prints all values in the list from head to tail."""
        current = self.head
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        print("Forward:  " + " <-> ".join(values))
        return self

    def print_values_backward(self):
        """Prints all values in the list from tail to head."""
        current = self.tail
        values = []
        while current:
            values.append(str(current.value))
            current = current.prev
        print("Backward: " + " <-> ".join(values))
        return self

    # --- Interview Puzzles ---

    def has_cycle(self):
        """
        Puzzle: How would you know if you have a circular linked list?
        Solution: Floyd's Cycle-Finding Algorithm (Tortoise and Hare).
        """
        if not self.head:
            return False
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def get_middle(self):
        """
        Puzzle: How would you get to the middle of the linked list?
        Solution: Two-runner approach. Fast moves twice as fast as slow.
        """
        if not self.head:
            return None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value

    def remove_duplicates(self):
        """
        Puzzle: How would you remove duplicate values from the list?
        Solution: Use a hash set to track seen values.
        """
        if not self.head:
            return self
        seen = set()
        current = self.head
        while current:
            if current.value in seen:
                # Remove this node
                node_to_remove = current
                current = current.next # Advance before removal
                
                if node_to_remove.prev:
                    node_to_remove.prev.next = node_to_remove.next
                else:
                    self.head = node_to_remove.next
                
                if node_to_remove.next:
                    node_to_remove.next.prev = node_to_remove.prev
                else:
                    self.tail = node_to_remove.prev
            else:
                seen.add(current.value)
                current = current.next
        return self

    def reverse(self):
        """
        Puzzle: How would you reverse the values in the list?
        Solution: Swap next and prev pointers for every node and swap head/tail.
        """
        current = self.head
        self.tail = self.head
        
        while current:
            # Swap pointers
            current.prev, current.next = current.next, current.prev
            
            # Move to next node (which is current.prev after swap)
            if not current.prev: # This was the original tail, now new head
                self.head = current
            current = current.prev
            
        return self


# --- Demonstration ---
if __name__ == "__main__":
    print("--- Doubly Linked List Demo ---")
    dlist = DoublyLinkedList()
    
    print("Adding values...")
    dlist.add_to_back(10).add_to_back(20).add_to_front(5).add_to_back(30)
    dlist.print_values()
    dlist.print_values_backward()

    print("\nInserting 15 at index 2...")
    dlist.insert_at(15, 2)
    dlist.print_values()

    print("\nRemoving value 20...")
    dlist.remove_val(20)
    dlist.print_values()

    print("\nMiddle elements:", dlist.get_middle())

    print("\nTesting duplicate removal (adding 10 and 30 again)...")
    dlist.add_to_back(10).add_to_back(30)
    dlist.print_values()
    dlist.remove_duplicates()
    dlist.print_values()

    print("\nReversing the list...")
    dlist.reverse()
    dlist.print_values()
    dlist.print_values_backward()

    print("\nChecking for cycle (should be False):", dlist.has_cycle())
