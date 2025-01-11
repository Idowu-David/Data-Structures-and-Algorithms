class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    # ===========================INSERT ALGORITHMS=============================    
    
    def insert_at_beginning(self, value):
        """Inserts a node at the beginning of the dll"""
        new = Node(value)
        if self.head is None: # No node in the list
            self.head = self.tail = new
        # Make new node the head in an existing list
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
        self.size += 1
        
    def insert_at_end(self, value):
        """Inserts a new node to the end of a dll"""
        new = Node(value)
        if self.head is None: # if DLL is empty
            self.head = self.tail = new
        else:
            new = Node(value)
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
        self.size += 1
        
    def insert_at_position(self, value, position):
        """Insert a node at a specified position"""
        if position > self.size:
            raise ValueError("Position greater than size of the list")
        if position < 0:
            raise ValueError("Position cannot be negative")
        if position == self.size:
            self.insert_at_end(value)
            
        new = Node(value)
        if position == 0:   # Add node at the beginning
            self.insert_at_beginning(value)
        else:
            current = self.head
            for _ in range(position):
                current = current.next
            prev = current.prev
            new.next = current
            current.prev = new
            new.prev = prev
            prev.next = new
        self.size += 1
        
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
        pass                        
                
                    
    def __str__(self):
        """Prints the singly linked list"""
        if self.head is None:
            return "Empty list"
        current = self.head
        st = ""
        while current:
            st += str(current.value)
            st += " <-> "
            current = current.next
        st += "None"
        return st
    

 # Initialize the list
node = DoublyLinkedList()
print(node)

node.insert_at_position(3, 0)
print(node)
node.insert_at_position(2, 1)
print(node)
node.insert_at_beginning(8)
print(node)
node.insert_at_end(4)
print(node)
node.insert_at_position(1, 3)
print(node)
node.delete(3)
print(node)
node.delete(2)
print(node)
node.delete(8)
print(node)
node.delete(4)
print(node)
node.delete(5)
print(node)