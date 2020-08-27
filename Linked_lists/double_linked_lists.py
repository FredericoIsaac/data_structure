class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class Double_linked_list:
    def __init__(self):
        self.head = None

    def print_list(self):
        """ Ill print the list """
        # Create a variable that is the current node
        trav = self.head
        # While not in the head of the linked list, print
        while trav:
            print(trav.data, end="-")
            # Pass to the next node
            trav = trav.next
        print()

    def append(self, data):
        """
        Append new values to the double linked list (at the end)
        """
        # if double linked list empty
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
            
        else:
            new_node = Node(data)
            current_node = self.head

            while current_node.next:
                current_node = current_node.next
            
            current_node.next = new_node
            new_node.prev = current_node
            
    def prepend(self, data):
        """
        Add a new node at the beggining of the double linked list
        """
        # if double linked list is empty
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            new_node.prev = None
    
    def add_after_node(self, key, data):
        """
        Ill add between nodes, after the key given
        input key is a data value
        """
        current_node = self.head
        
        while current_node:
            if current_node.next is None and current_node.data == key:
                self.append(data)
                return
            elif current_node.data == key:
                new_node = Node(data)
                next_node = current_node.next
                
                current_node.next = new_node

                new_node.next = next_node
                new_node.prev = current_node

                next_node.prev = new_node
                return

            current_node = current_node.next
    
    def add_before_node(self, key, data):
        """
        Ill add between node, before the key given
        """
        current_node = self.head

        while current_node:
            # if the key is in the beggining of the double linked list
            if current_node.prev is None and current_node.data == key:
                self.prepend(data)
                return
            elif current_node.data == key:
                new_node = Node(data)
                prev_node = current_node.prev

                current_node.prev = new_node
                prev_node.next = new_node
                new_node.prev = prev_node
                new_node.next = current_node
                return
            
            current_node = current_node.next
        
        raise ValueError("Key not found")       

    def delete_element(self, key):
        """
        Delete and element find by key
        """
        current_node = self.head

        while current_node:
            # Primeiro node vai ser eliminado
            if current_node.data == key and current_node.prev is None:
                # Only one node in the double linked list
                if current_node.next is None:
                    current_node = None
                    self.head = None
                    return

                next_node = current_node.next
                next_node.prev = None
                current_node = None
                self.head = next_node
                return

            # Ultimo node vai ser eliminado
            elif current_node.data == key and current_node.next is None:
                prev_node = current_node.prev
                prev_node.next = None
                current_node = None
                return
                
            # Node do meio vao ser eliminados
            elif current_node.data == key:
                prev_node = current_node.prev
                next_node = current_node.next

                prev_node.next = next_node
                next_node.prev = prev_node
                current_node = None  
                return              

            current_node = current_node.next

        raise ValueError("Key not fount, or double linked list empty")

    def reverse(self):
        # Create a variable that indicates the current node
        trav = self.head
        # Create a temporary pointer
        tmp = trav
        # iterate over the linked list
        while trav is not None:
            # Indicates to the temporary pointer the previous pointer of the current node
            tmp = trav.prev
            # Next flip the current previous ponter 
            trav.prev = trav.next
            # Flip the current next pointer
            trav.next = tmp
            # Iterate over loop (normally is next but is reversing)
            trav = trav.prev
            
        # If final of the linked list (tmp = None)
        if tmp is not None:
            # Change head of the linked list to the last element of the linked list
            self.head = tmp.prev


dllist = Double_linked_list()

dllist.prepend(1)
# 1
dllist.append(2)
# 2
dllist.append(3)
# 3
dllist.print_list()
# 1-2-3-
dllist.prepend(0)
# 0-1-2-3-
dllist.add_after_node(2,2)
# 0-1-2-2-3-
dllist.add_before_node(3,5)
# 0-1-2-2-5-3-
dllist.delete_element(2)
dllist.print_list()
# 0-1-2-5-3-
dllist.reverse()
dllist.print_list()
# 3-5-2-1-0

