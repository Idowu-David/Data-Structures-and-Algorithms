"""
This module implements a singly linked list and provides core operations such as insertion, deletion, and search.

Classes:
    - Node: Represents an individual element (node) in the linked list.
    - SinglyLinkedList: Represents the linked list and provides methods for managing it.

Methods:
    - insert_at_beginning: Adds a new node at the start of the list.
    - insert_at_end: Adds a new node at the end of the list.
    - insert_at_position: Adds a new node at a specific position in the list.
    - delete: Removes the first occurrence of a node with the specified value.
    - search: Checks if a value exists in the list.
    - __str__: Returns a string representation of the list.

Usage Example:
    >>> sll = SinglyLinkedList()
    >>> sll.insert_at_end(10)
    >>> sll.insert_at_end(20)
    >>> print(sll)  # Output: 10 -> 20 -> None
    >>> sll.delete(10)
    >>> print(sll)  # Output: 20 -> None
    >>> print(sll.search(20))  # Output: True
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  
        self.size = 0         
        
    # ===========================INSERT ALGORITHMS=============================
        
    def insert_at_beginning(self, value):
        """Inserts a new node to an empty SLL"""
        new = Node(value)
        # no node in the SLL
        if self.head == None:
            self.head = self.tail = new
        # make new node the head in an existing list
        else:
            new.next = self.head
            self.head = new
        self.size += 1
    
    def insert_at_end(self, value):
        """Inserts a new node to the end of a SLL"""
        new = Node(value)
        if self.head == None: # if SLL is empty
            self.insert_at_beginning(value)
        else:
            self.tail.next = new
            self.tail = new
        self.size += 1
            
    def insert_at_position(self, value, position):
        """Insert a node at a specified position"""
        # To insert at position, cases to consider are:
        #  i. Position given is the head
        # ii. Insert after the tail -> insert at end
        # iii. Insert in a position < 0 or position > length of the list -> invalid positionnew = Node(value)
        if position >= 0:
            new = Node(value)
            if position == 0: # insert at beginning
                    new.next = self.head
                    self.head = new
                    self.size += 1
            else:
                current = self.head
                count = 0
                if current != None:
                    while current.next:
                        if count < position - 1:
                            current = current.next
                            count += 1
                        else:
                            break
                    if count == position - 1:   # Checks if there was a traversal, so it validates the position to be added
                        if current.next == None:
                            current.next = new
                            self.tail = new
                        else:
                            new.next = current.next
                            current.next = new
                        self.size += 1
                    else:   # If no traversal, then the position specified is outside the list
                        raise IndexError(f"Invalid Position: {position} exceeds list size")
                else:
                        raise IndexError(f"Invalid Position: {position} exceeds list size")
                    
        else:
            raise IndexError("Invalid Position: position cannot be negative")
        
    # ===========================SEARCH ALGORITHMS=============================
    def search(self, value):
        """Search for a value or node in the linked list"""
        current = self.head
        if current == None:
            raise ValueError("Linked List is empty")
        count = 0
        positions = []
        while current:
            if current.value == value:
                positions.append(count)
            current = current.next
            count += 1
        return positions if positions else -1
                

    # ===========================DELETE ALGORITHMS=============================
    def delete(self, value):
        """Deletes the first occurence of a Node in the linked list"""
        if self.head == None:
            raise ValueError("Linked List is empty")
        
        current = self.head
        if current.value == value: # if the node to delete is the head
            self.head = self.head.next
            current = None
            self.size -= 1
            return True               

        prev = current
        while current.next:
            if current.value == value:
                prev.next = current.next
                current = prev = None  
                self.size -= 1              
                return True
            prev = current
            current = current.next
            if current.next == None and current.value == value:
                current = prev.next = None
                self.size -= 1
                return True
        raise ValueError("Node not in the Linked List")
                
                                         
    def __str__(self):
        """Prints the singly linked list"""
        current = self.head
        st = ""
        while current:
            st += str(current.value)
            st += " -> "
            current = current.next
        st += "None"
        return st
    
    
# node = SinglyLinkedList()

# node.insert_at_beginning(10)
# node.insert_at_beginning(11)
# node.insert_at_beginning(5)
# node.insert_at_beginning(8)
# node.insert_at_end(9)
# node.insert_at_position(6, 2)
# print(node)
# print(node.delete(8))
# print(node)

# Initialize the singly linked list
node = SinglyLinkedList()
node.insert_at_beginning(1)
node.insert_at_beginning(10)
node.insert_at_beginning(3)
node.insert_at_beginning(9)
node.insert_at_end(7)
print(node)
print(node.size)
node.delete(7)
print(node)
print(node.size)
node.delete(10)
print(node)
print(node.size)


