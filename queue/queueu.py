
# dequeue() - remove the head element and returns is value
# peek() - look at the head element but dont remove
# isEmpty() - test if the queue is empty
# size() - returns the number of items in the queue

class Node:
    def __init__(self, value= None):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.num_elements = 0
    
    def push_stack(self, value):
        """
        Add an element to the top of the stack (head)
        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node

        self.num_elements += 1

    def pop_stack(self):
        """
        Eliminate and return the top element of the stack (head)
        """
        if self.head is None:
            return None
        
        value = self.head.value
        self.head = self.head.next

        self.num_elements -= 1
        return value

    def peek_stack(self):
        return self.head.value
    
    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0       

        

class Queue:
    def __init__(self):
        # the first element of queue (the oldest)
        self.head = None
        # the last element of queue (the youngest)
        self.tail = None
        # keep track of the items in the queueu
        self.num_elements = 0

    def enqueue(self, value):
        """
        Add a element to the tail
        """
        new_node = Node(value)

        # If queue is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

        # increment size
        self.num_elements += 1
        return

    def dequeue(self):
        """
        Eliminates the first element of the queue (the oldest)
        """
        # if queueu is empty
        if self.head is None:
            raise ValueError("Cannot dequeue, queue is empty")

        value = self.head.value
        self.head = self.head.next

        self.num_elements -= 1
        return value

    def size(self):
        return self.num_elements

    def isEmpty(self):
        return self.num_elements == 0  

    def peek(self):
        return self.head.value      

    def reverse_queue(self):
        """
        Reverse the current queue
        """
        if self.head is None:
            raise ValueError("Queueu is empty, nothing to reverse")

        stack = Stack()

        while not self.isEmpty():
            stack.push_stack(self.dequeue())

        while not stack.is_empty():
            self.enqueue(stack.pop_stack())



def test_function(test_case):
    queue = Queue()
    for num in test_case:
        queue.enqueue(num)
    
    queue.reverse_queue()
    index = len(test_case) - 1
    while not queue.isEmpty():
        removed = queue.dequeue()
        if removed != test_case[index]:
            print("Fail")
            return
        else:
            index -= 1
    print("Pass")

test_case_1 = [1, 2, 3, 4]
test_function(test_case_1)

test_case_2 = [1]
test_function(test_case_2)