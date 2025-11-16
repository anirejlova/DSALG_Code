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

    # Traverse BST until target is found and delete it
    # 3 cases: node has no child/subtree, one child/subtree, two children/subtrees
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, curr_node, key):
        if curr_node is None:
            return curr_node  # base case: tree is empty

        if key < curr_node.value:  # go to left subtree
            curr_node.left = self._delete(curr_node.left, key)
        elif key > curr_node.value:  # go to right subtree
            curr_node.right = self._delete(curr_node.right, key)
        else:  # node with one or no child
            if curr_node.left is None:
                temp = curr_node.right
                curr_node = None  # delete node
                return temp
            elif curr_node.right is None:
                temp = curr_node.left
                curr_node = None  # delete node
                return temp
            # Node with two children: get inorder successor (smalleest/leftmoset in right subtree) to replace the value of the deleted node)
            temp = self._min_value_node(curr_node.right)
            curr_node.value = (
                temp.value
            )  # copy the inorder successor's content to this node
            curr_node.right = self._delete(
                curr_node.right, temp.value
            )  # delete the inorder successor
        return curr_node

    def _min_value_node(self, node):
        # locate smallest/leftmost node in the right subtree
        current = node
        while current.left is not None:
            current = current.left
        return current
