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
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    
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
                
            







dllist = Double_linked_list()

dllist.prepend(1)
dllist.print_list()
dllist.append(2)
dllist.print_list()
dllist.append(3)
dllist.print_list()
dllist.prepend(0)
dllist.print_list()
dllist.add_after_node(2,2)
dllist.print_list()