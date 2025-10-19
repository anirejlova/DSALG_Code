# Implement a Queue using an Array/List:
class Queue:
    def __init__(self):
        self.items = []
        self.max_size = 5

    def get_items(self):
        return self.items

    # Add an element to the tail (rear) of the queue
    def enqueue(self, item):
        pass

    # Remove the element from the head (front) of the queue
    def dequeue(self):
        pass

    #  View the element at the head of the queue without removing it
    def peek_head(self):
        pass

    #  Return the number of elements in the queue
    def length(self):
        pass

    # Design an algorithm to reverse a Queue using Stacks and Queues.
    # (Example: Convert Queue “12345” into Queue “54321”.)
    def reverse(self):
        # take things from FIFO to LIFO
        pass


# Implement a Stack using an Array/List:
class Stack:
    def __init__(self):
        self.items = []
        self.max_size = 5

    # Add an element to the top of the stack
    def push(self, item):
        pass

    #  Remove the element from the top of the stack
    def pop(self):
        pass

    # View the element at the top of the stack without removing it
    def peek(self):
        pass

    # Return the number of elements in the stack
    def length(self):
        pass


#  Implement a Circular Queue using an Array or List
class CircularQueue(Queue):
    pass


# run
q = Queue()
