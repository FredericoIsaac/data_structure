class Node:
    def __init__(self, value= None):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        """
        Add elements to the top of the stack
        """
        # Create a node with the value
        new_node = Node(value)

        # Checks if stack is empty
        if self.head is None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head = new_node

        # add an element to the stack
        self.num_elements += 1
    
    def size(self):
        """
        Give the size of the stack
        """
        return self.num_elements
    
    def is_empty(self):
        """
        True if stack is empty
        """
        return self.num_elements == 0
    
    def pop(self):
        """
        Eliminates and return the first element of the stack
        """
        if self.is_empty():
            return None

        first_element = self.head.data

        self.head = self.head.next
        self.num_elements -= 1

        return first_element

    def peek(self):
        """
        Return the first element but dont eliminate
        """
        if self.is_empty():
            return None
        
        return self.head.data



        
