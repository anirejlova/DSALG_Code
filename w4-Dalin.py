# SINGLY LINKED LIST (SLL) - Šmídův řetězový uzel v Javě or sum like that??
class Node: # each node has two attributes: data (its value) and next (pointer to the next node)
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # head points to the first node in the list - curr none

# CRUDS rules
    # insert method - new node containing data at the end of the list
    def insert(self, data):
        new_node = Node(data)  # create a new node
        if not self.head: # Special case if list is empty
            self.head = new_node  # set head to new node
        else:
            current = self.head  # start at the head
            while current.next:  # traverse to the last node
                current = current.next
            current.next = new_node  # link the last node to the new node
    
    # search method - SLL is traversed till its end to find target data
    def search(self, target_data):
        current = self.head  # start at the head
        while current:  # traverse the list
            if current.data == target_data:  # check if current node's data matches target
                return True  # target found
            current = current.next  # move to the next node
        return False  # target not found
    
    # delete method - go through SLL till its end to find target data and remove it
    def delete(self, target_data):
        if not self.head:  # if list is empty
            return
        
        if self.head.data == target_data: # deleting head node if it matches taget
            self.head = self.head.next  # set head as the next node
            return
        
        current = self.head  # start at the head
        while current.next:  # traverse the list
            if current.next.data == target_data:  # check if next node's data matches target
                current.next = current.next.next  # delete the node
                return
            current = current.next  # move to the next node

    # traverse method - SLL traversed till its end to print all data
    def traverse(self):
        current = self.head  # start at the head
        while current:  # traverse the list
            print(current.data)
            current = current.next  # move to the next node

# Sorting algorithm for SLL
    # basic item swap operation
    def swap_nodes(self, a, b):
        temp = a.data
        a.data = b.data
        b.data = temp

    # compare neighboring nodes and swap if needed
    def bubble_sort(self):
        if self.head is None:
            return
        
        swapped = True # flag indicator to stop earlier
        while swapped:
            swapped = False
            current = self.head
            while current.next: # traverse till the second last node
                if current.data > current.next.data: # compare current node with next node
                    self.swap_nodes(current, current.next)
                    swapped = True # set flag to True if swap happened
                current = current.next

# run
# CRUDS test
sll = SinglyLinkedList()
sll.insert(10)
sll.insert(20)
sll.insert(30)
print("Traversing the list:")
sll.traverse()
print("\nSearching for 20:", sll.search(20))
print("Searching for 40:", sll.search(40))
sll.delete(20)
print("\nTraversing the list after deleting 20:")
sll.traverse()

# Sorting test
sll.insert(0)
sll.insert(50)
sll.insert(40)
sll.insert(20)
print("\nTraversing the unsorted list:")
sll.traverse()
print("\nTraversing the sorted list (bubble):")
sll.bubble_sort()
sll.traverse()