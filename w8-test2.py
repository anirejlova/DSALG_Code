class Node:  # each node has two attributes: data (its value) and next (pointer to the next node)
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
        if not self.head:  # Special case if list is empty
            self.head = new_node  # set head to new node
        else:
            current = self.head  # start at the head
            while current.next:  # traverse to the last node
                current = current.next
            current.next = new_node  # link the last node to the new node

    # traverse method - SLL traversed till its end to print all data
    def traverse(self):
        current = self.head  # start at the head
        while current:  # traverse the list
            print(current.data)
            current = current.next  # move to the next node
            
    # Merge two sorted SLLs into one sorted SLL
    def split(self, big_list):
        pos = SinglyLinkedList()
        neg = SinglyLinkedList()
        n = big_list.head
        while n is not None: # traverse list
            if n.data >= 0:
                pos.insert(n.data)
            else: # n1.data <= n2.data
                neg.insert(n.data)
            n = n.next
        return pos, neg


    

#run
sll = SinglyLinkedList()
sll.insert(4)
sll.insert(-5)
sll.insert(0)
sll.insert(-7)
sll.insert(6)
print("Traversing the list:")
sll.traverse()


print("\nSplit Lists:")
pos_list, neg_list = sll.split(sll)
print("\nPositive/Zero SLL:")
pos_list.traverse()
print("\nNegative SLL:")
neg_list.traverse()