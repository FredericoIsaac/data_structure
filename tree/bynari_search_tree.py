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
        """
        Find recursively the data and return boolean
        """
        # Check if tree is empty
        if self.root == None:
            return None
        
        is_found = self._find(data, self.root)
        if is_found:
            return True
        return False

    def _find(self, data, cur_node):

        # Base Case
        if cur_node.data == data:
            return True

        if data < cur_node.data and cur_node.left:
            return self._find(data, cur_node.left)
        elif data > cur_node.data and cur_node.right:
            return self._find(data, cur_node.right)

    def inorder_print_tree(self):
        if self.root:
            self._inorder_print_tree(self.root)

    def _inorder_print_tree(self, cur_node):
        if cur_node:
            self._inorder_print_tree(cur_node.left)
            print(cur_node.data)
            self._inorder_print_tree(cur_node.right)







bst = BinarySearchTree()

bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(9)


print(bst.find(9))
# True