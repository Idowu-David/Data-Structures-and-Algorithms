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
        if self.head == None: # No node in the list
            self.head = self.tail = new
        # Make new node the head in an existing list
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
        self.size += 1
        
    def insert_at_end(self, value):
        """Inserts a new node to the end of a dll"""
        if self.head == None: # if DLL is empty
            self.insert_at_beginning(value)
        else:
            new = Node(value)
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
        self.size += 1
        
    def insert_at_position(self, value, position):
        """Insert a node at a specified position"""
        pass
    
    def __str__(self):
        """Prints the singly linked list"""
        current = self.head
        st = ""
        while current:
            st += str(current.value)
            st += " <-> "
            current = current.next
        st += "None"
        return st
    
node = DoublyLinkedList()
node.insert_at_beginning(9)
node.insert_at_end(8)
node.insert_at_end(7)
node.insert_at_end(4)
node.insert_at_beginning(8)
print(node)
print("Size: ", node.size)
    
    

    


    
        