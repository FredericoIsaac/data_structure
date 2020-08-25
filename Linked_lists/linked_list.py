
# Create a Linked List

class Node:
    def __init__(self, value= None):
        self.value = value
        self.next = None

class Linked_list:
    def __init__(self):
        # Initialize with the first node of the list (head)
        self.head = None

    def create_linked_list_iteration(self, input_list):
        """
        Given a list of values, transform into a linked list
        input: input_list , a list of values
        """
        tail = None

        for value in input_list:

            # first iteration
            if self.head is None:
                self.head = Node(value)
                tail = self.head
            else:
                tail.next = Node(value)
                tail = tail.next # update tail
        return self.head

    def print_linked_list(self):
        """
        Print all values of the linked list
        """
        # Declare the current node has the beginning of the list
        current_node = self.head

        # while not the end of the linked list
        while current_node is not None:
            print(current_node.value)
            # Pass the current node to the next A -> B now B -> C
            current_node = current_node.next

    def linked_list_to_list(self):
        out_list = []

        node = self.head
        while node:
            out_list.append(node.value)
            node = node.next
        
        return out_list            

    def append(self, value):
        """
        Append a new node to the end of the linked list
        """
        # If linked list empty
        if self.head is None:
            self.head = Node(value)
            return
        
        node = self.head
        # while not the end of the linked list C -> None
        while node.next:
            node = node.next
        
        # End of the linked list
        node.next = Node(value)
        return

    def prepend_linked_list(self, value):
        """
        Prepend a value (in the beggining) of the linked list
        """
        # if linked list empty
        if self.head is None:
            self.head = Node(value)
            return
        # Create a new node 
        new_node = Node(value)
        # Link new node to the head of the linked list
        new_node.next = self.head
        # Change head to the new node, the new head
        self.head = new_node
        return 

    def insert_linked_list(self, value, position):
        """
        Insert value at pos position in the list.
        If pos is larger than teh legnth of the list, append to the end of the list
        A -> B -> C
        insert(D, 1)
        A -> D -> B -> C  
        """
        # if linked list empty
        if self.head is None:
            self.head = Node(value)
            return
        
        # If at the beggining of the linked list
        if position == 0:
            self.prepend_linked_list(value)
            return

        # Create a controler of the index
        index = 0
        node = self.head

        while node.next:
            prev_node = node
            node = node.next
            index += 1

            if index == position:
                new_node = Node(value)
                new_node.next = node
                prev_node.next = new_node
                return
        
        node.next = Node(value)
        return

    def search_linked_list(self, value):
        """
        Search a value in the linked list and return True or False
        """
        # Linked List empty
        if self.head is None:
            return False
        
        node = self.head
        while node:
            if node.value == value:
                return True
            
            node = node.next

        return False

    def remove_node(self, value):
        """
        Delete the first node with the desired data
        """
        # if linked list empty
        if self.head is None:
            raise ValueError("Linked list Empty")
        
        # if is the first node
        if self.head.value == value:
            self.head = self.head.next
            return

        node = self.head
        
        while node:
            prev_node = node
            node = node.next

            if node.value == value:
                prev_node.next = node.next
                node = None
        
        return

    def pop_linked_list(self):
        """
        Return the first node and remove it from the linked list
        """
        # if linked list empty
        if self.head is None:
            raise ValueError("Linked list empty")

        node = self.head
        self.head = self.head.next

        return node.value



    def size_linked_list(self):
        """
        Return the size of the linked list
        """
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        
        return count

    def reversing_linked_list(self):
        """
        Reverse the inputted linked list
        """
        if self.head is None:
            raise ValueError("Link List empty, nothing to reverse")
        elif self.size_linked_list() == 1:
            return

        current_node = self.head
        last_node = None
        
        while current_node:
            after_node = current_node.next
            current_node.next = last_node
            last_node = current_node
            current_node = after_node

        self.head = last_node 
        return        



my_linked_list = Linked_list()
my_linked_list.create_linked_list_iteration([5,6,8])
my_linked_list.print_linked_list() # 5\n 6\n 8
print()
my_linked_list.append(1)
my_linked_list.print_linked_list() # 5\n 6\n 8\n 1
print(my_linked_list.linked_list_to_list())
my_linked_list.prepend_linked_list(0)
print(my_linked_list.linked_list_to_list()) # [0,5,6,8,1]
print(my_linked_list.search_linked_list(6)) # True
print(my_linked_list.search_linked_list(10)) # False
my_linked_list.remove_node(1)
print(my_linked_list.linked_list_to_list()) # [0,5,6,8]
print(my_linked_list.pop_linked_list()) # 0
my_linked_list.insert_linked_list(1,10)
print(my_linked_list.linked_list_to_list()) # [5,6,8,1]
my_linked_list.insert_linked_list(1,0)
print(my_linked_list.linked_list_to_list()) # [1,5,6,8,1]
my_linked_list.insert_linked_list(1,2)
print(my_linked_list.linked_list_to_list()) # [1,5,1,6,8,1]
print(my_linked_list.size_linked_list())
my_linked_list.reversing_linked_list()
print(my_linked_list.linked_list_to_list())