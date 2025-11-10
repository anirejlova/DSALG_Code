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
    