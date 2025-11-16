# BINARY SEARCH TREES
# the public method calling the same-called private method with the root node as argument is RECURSION


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

    # Implemented traverse method to output all data items
    # 2 ways: breadth-first and depth-first (pre-order, in-order, post-order)

    # DEPTH-FIRST TRAVERSAL METHODS
    def inorder(self):
        self._inorder(self.root)
        print()  # for newline after traversal

    def _inorder(self, curr_node):
        if curr_node is not None:
            self._inorder(curr_node.left)
            print(curr_node.value, end=" ")
            self._inorder(curr_node.right)

    def preorder(self):
        self._preorder(self.root)
        print()  # for newline after traversal

    def _preorder(self, curr_node):
        if curr_node is not None:
            print(curr_node.value, end=" ")
            self._preorder(curr_node.left)
            self._preorder(curr_node.right)

    def postorder(self):
        self._postorder(self.root)
        print()  # for newline after traversal

    def _postorder(self, curr_node):
        if curr_node is not None:
            self._postorder(curr_node.left)
            self._postorder(curr_node.right)
            print(curr_node.value, end=" ")

    # BREADTH-FIRST TRAVERSAL
    def breadth_first(self):
        result = []  # list to store the order of traversal
        queue = [self.root]

        while queue:
            curr_node = queue.pop(0)
            if curr_node:
                result.append(curr_node.value)
                queue.append(curr_node.left)
                queue.append(curr_node.right)
        print(result)

    # Implementing the traversal methods iteratively, which will keep track of the nodes using a stack.
    def preorder_iter(self):
        # For the preOrder traversal (VLR), after visiting a node's value, we push its right and then its left child onto the stack. Given the nature of a stack- FILO, the left child will be the first to be popped.
        if not self.root:
            return []

        stack, output = [self.root], []
        while stack:
            node = stack.pop()
            if node:
                output.append(node.value)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        print(output)  # return output

    def inorder_iter(self):
        # For the inOrder traversal (LVR), we keep pushing the left child nodes onto the stack. When a node has no left child (or its left child is already visited), its value will be visited and its right child will be pushed onto the stack.
        stack, output = [], []
        current = self.root
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            output.append(current.value)
            current = current.right
        print(output)  # return output

    def postorder_iter(self):
        # For the postOrder traversal (LRV), we use two stacks. The first stack is used to traverse all the nodes and sort their sequence before pushing them onto the second stack. Once all the nodes have been visited and the first stack is empty, we visit and output the values of the nodes from the second stack, following FILO.
        if not self.root:
            return []
        stack1, stack2 = [self.root], []

        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        output = []
        while stack2:
            node = stack2.pop()
            output.append(node.value)
        print(output)  # return output


# test BST
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)
print("Inorder traversal:")
bst.inorder()
print("Preorder traversal:")
bst.preorder()
print("Postorder traversal:")
bst.postorder()

print("Breadth-first traversal:")
bst.breadth_first()

print("Search for 40:", bst.search(40))
print("Search for 100:", bst.search(100))

print("Delete 20:")
bst.delete(20)

print("Inorder traversal after deleting 20:")
bst.inorder()

# Post-order: visit left subtree, then right subtree, then the node itself. Leaves come first, parents last. For your tree it prints: 20 40 30 60 80 70 50

# Breadth-first (level-order): visit nodes level by level from the root, left to right, using a queue. For your tree it produces: [50, 30, 70, 20, 40, 60, 80]

# EXCERCISE 2 - iteration
print()
print("Iterative inorder traversal:")
bst.inorder_iter()
print("Iterative preorder traversal:")
bst.preorder_iter()
print("Iterative postorder traversal:")
bst.postorder_iter()
