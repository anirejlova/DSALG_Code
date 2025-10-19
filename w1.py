# Implement a Queue using an Array/List:
class Queue:
    def __init__(self):
        self.items = []
        self.max_size = 5

    def get_items(self):
        return self.items

    # Add an element to the tail (rear) of the queue
    def enqueue(self, item):
        print("Enqueue")
        self.items.append(item)

    # Remove the element from the head (front) of the queue
    def dequeue(self):
        print("Dequeue")
        if not self.length() == 0:
            self.items.pop(0)
            print(self.items)
        raise IndexError("Cannot delete from an empty queue.")

    #  View the element at the head of the queue without removing it
    def peek_head(self):
        print("Peek")
        if not self.length() == 0:
            print(self.items[0])
        raise IndexError("Cannot peek an empty queue.")

    #  Return the number of elements in the queue
    def length(self):
        print("Length: " + str(len(self.items)))
        return len(self.items)

    # Design an algorithm to reverse a Queue using Stacks and Queues.
    # (Example: Convert Queue “12345” into Queue “54321”.)
    def reverse(self):
        # take things from FIFO to LIFO
        stack = Stack()  # we need to create a stack to put our items in
        while self.items > 0:  # can't be empty
            element = self.dequeue()  # take from queue
            stack.push(element)  # put in stack
        while stack.length() > 0:  # can't be empty
            element = stack.pop()  # take from stack
            self.enqueue(element)  # put in queue
            # Now the queue is reversed
        print("Reversed Queue:")
        self.peek()


# Implement a Stack using an Array/List:
class Stack:
    def __init__(self):
        self.items = []

    # Add an element to the top of the stack
    def push(self, item):
        print("Push")
        self.items.append(item)
        print(self.items)

    #  Remove the element from the top of the stack
    def pop(self):
        print("Pop")
        if not len(self.items) == 0:
            self.items.pop()
            print(self.items)
        else:
            print("Stack is empty")

    # View the element at the top of the stack without removing it
    def peek(self):
        print("Peek")
        if not len(self.items) == 0:
            print(self.items[-1])
        else:
            print("Stack is empty")

    # Return the number of elements in the stack
    def length(self):
        print("Length")
        return len(self.items)
        print(len(self.items))


#  Implement a Circular Queue using an Array or List
class CircularQueue(Queue):
    def __init__(self):
        super().__init__()


# run
q = Queue()
for i in range(1, 4):
    q.enqueue(i)
print("Initial queue data:", q.get_items())
q.enqueue(5)
print("After enqueue 5:", q.get_items())
q.dequeue()
print("After dequeue:", q.get_items())
q.peek_head()
q.length()
# q.reverse()

# s = Stack()
# print("for loop for data input:")
# for i in range(1, 5):
#     s.push(i)
# s.pop()
# s.peek()
# s.length()
