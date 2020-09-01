class Node:
    def __init__(self, data= None):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        """
        Add a node respecting the rules of BTS
        """
        # Empty Tree
        if self.root == None:
            self.root = Node(data)
        else:
            # Call to a recursive function to traverse the tree
            self._insert(data, self.root)

    def _insert(self, data, cur_node):
        """
        Traverse the tree using recursive until find the right place
        """
        if data < cur_node.data:
            if cur_node.left is None:
                cur_node.left = Node(data)
                return
            else:
                self._insert(data, cur_node.left)
        
        elif data > cur_node.data:
            if cur_node.right is None:
                cur_node.right = Node(data)
                return
            else:
                self._insert(data, cur_node.right)
        else:
            print("Value is already present in tree")

    def find(self, data):
        pass




bst = BinarySearchTree()

bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(9)