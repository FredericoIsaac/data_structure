class Binary_tree:
    def __init__(self, root= None):
        self.key = root
        self.leftChild = None
        self.rightChild = None
    
    def insertLeft(self, value):
        """
        Create a new binary_tree and add to the left of the current tree
        """
        # if left is empty
        if self.leftChild == None:
            # Create a new tree object
            self.leftChild = Binary_tree(value)
        else:
            # Insert the new node linked to the root, the current node go down one level
            new_node = Binary_tree(value)
            new_node.leftChild = self.leftChild
            self.leftChild = new_node

    def insertRight(self, value):
        """
        Create a new binary object an add the the right of the root
        """
        new_node = Binary_tree(value)

        if self.rightChild == None:
            self.rightChild = new_node
        else:
            new_node.rightChild = self.rightChild
            self.rightChild = new_node

    def getRightChild(self):
        return self.rightChild.value
    
    def getLeftChild(self):
        return self.leftChild.value
    
    def setRootVal(self, value):
        self.key = value
    
    def getRootVal(self):
        return self.key
