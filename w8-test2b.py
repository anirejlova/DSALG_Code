class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BST:
    def __init__(self):
        self.root = None  # considerer empty tree

    # A new Node containing the key value is created and inserted into the BST, ensuring compliance with the BST's definition.
    def insert(self, key):
        if self.root is None:  # if BST is empty
            self.root = Node(key)  # create root node
        else:
            self._insert(self.root, key)  # call helper method

    def _insert(self, curr_node, key):
        if key < curr_node.value:  # go to left subtree
            if (
                curr_node.left is None
            ):  # stopping case - if subtree is empty, insert new node to the empty space
                curr_node.left = Node(key)
            else:
                self._insert(curr_node.left, key)  # recursive call on left subtree
        elif key > curr_node.value:  # go to right subtree
            if curr_node.right is None:
                curr_node.right = Node(key)
            else:
                self._insert(curr_node.right, key)
        else:
            print("Value already exists in the tree.")
            
    def postorder(self): #LRV
        self._postorder(self.root)
        print()  # for newline after traversal

    def _postorder(self, curr_node):
        if curr_node is not None:
            self._postorder(curr_node.left)
            self._postorder(curr_node.right)
            print(curr_node.value, end=" ")
            
    def nodes_in_range(self):
        count = 0
        curr_node = self.root
        if 7<=curr_node.value<=18:
            count += 1
        return count


#run
bst = BST()
bst.insert(11)
bst.insert(6)
bst.insert(17)
bst.insert(3)
bst.insert(8)
bst.insert(15)
bst.insert(19)
bst.insert(18)
print("Postorder traversal:")
bst.postorder()
print("Number of nodes in range 7-18:")
print(bst.nodes_in_range())



