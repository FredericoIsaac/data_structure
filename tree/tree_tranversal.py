class Stack(object):
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    def size(self):
        return len(self.items)
    def __len__(self):
        return self.size()

class Queue(object):
    """
    To help Level-order Traversal
    """
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        """
        Ill return the top of the queue (the first in)
        """
        if not self.is_empty():
            return self.items[-1].value
    
    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Node:
    def __init__(self, value= None):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        """
        Print out the tree with the type of algorithms (traversal_type) we ill print out 
        and call the function preorder_print
        """
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)
        elif traversal_type == "reverse_levelorder":
            return self.reverse_levelorder_print(tree.root)
        else:
            # Error check
            print("Traversal type" + str(traversal_type) + " is not supported")
            return False

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
    def inorder_print(self, start, traversal):
        if start:
            traversal = self.preorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def levelorder_print(self, start):
        if start is None:
            return
        queue = Queue()
        # Root level
        queue.enqueue(start)
        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal
        
    def reverse_levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)
        stack = Stack()

        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"

        return traversal

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    def size_(self, node):
        if node is None:
            return 0

        return 1 + self.size_(node.left) + self.size_(node.right)

    def size(self):
        if self.root is None:
            return 0

        stack = Stack()
        stack.push(self.root)
        size = 1

        while stack:
            node = stack.pop()
            if node.left:
                size +=1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size

    def diameter_of_binary_tree(self, root):
        return self.diameter_of_binary_tree_func(root)[1]
    
    def diameter_of_binary_tree_func(self, root):
        if root is None:
            return 0, 0

        left_height, left_diameter = self.diameter_of_binary_tree_func(root.left)
        right_height, right_diameter = self.diameter_of_binary_tree_func(root.right)

        current_height = max(left_height, right_height) + 1
        height_diameter = left_height + right_height
        current_diameter = max(left_diameter, right_diameter, height_diameter)

        return current_height, current_diameter        

            




tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("preorder"))
# 1-2-4-5-3-6-7-
print(tree.print_tree("inorder"))
# 4-2-5-1-6-3-7-
print(tree.print_tree("postorder"))
# 4-5-2-6-7-3-1-
print(tree.print_tree("levelorder"))
# 1-2-3-4-5-6-7-
print(tree.print_tree("reverse_levelorder"))
# 4-5-6-7-2-3-1-

print(tree.height(tree.root))
# 2
print(tree.size())
# 7
print(tree.size_(tree.root))
# 7

print(tree.diameter_of_binary_tree(tree.root))
# 4