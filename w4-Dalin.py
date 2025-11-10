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