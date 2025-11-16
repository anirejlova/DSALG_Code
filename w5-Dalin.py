# BINARY SEARCH TREES


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

    # Traverse BST until a leaf node is reached to locate the target
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, curr_node, key):
        if curr_node is None:  # BST is empty
            return False
        if key == curr_node.value:  # target found
            return True
        elif key < curr_node.value:  # go to left subtree
            return self._search(curr_node.left, key)
        else:  # go to right subtree
            return self._search(curr_node.right, key)
