# Implement a Queue using an Array/List:
class Queue:
    def __init__(self):
        self.items = []
        self.max_size = 5

    def get_items(self):
        return self.items

    # Add an element to the tail (rear) of the queue
    def enqueue(self, item):
        if self.length() >= self.max_size:
            raise OverflowError("Queue is full. Cannot enqueue")
        self.items.append(item)

    # Remove the element from the head (front) of the queue
    def dequeue(self):
        if self.length() == 0:
            raise IndexError("Queue is empty. Cannot dequeue")
        return self.items.pop(0)

    #  View the element at the head of the queue without removing it
    def peek_head(self):
        print("The first item is: " + str(self.items[0]))
        #  raise QueueEmptyError("Cannot peek from an empty queue.")

    #  Return the number of elements in the queue
    def length(self):
        return len(self.items)

    # Design an algorithm to reverse a Queue using Stacks and Queues.
    # (Example: Convert Queue “12345” into Queue “54321”.)
    def reverse(self):
        # take things from FIFO to LIFO to reverse-FIFO
        print("Queue before reverse: " + str(self.get_items()))
        stack = Stack()  # create stack to use as odkládací polička
        while self.length() != 0:
            element = self.dequeue()
            stack.push(element)
        while stack.length() != 0:
            element = stack.pop()
            self.enqueue(element)
        print("Queue after reverse: " + str(self.get_items()))

    def __str__(self):
        return (
            "The queue size is: "
            + str(self.length())
            + "; Values: "
            + str(self.get_items())
        )


# Implement a Stack using an Array/List:
class Stack:
    def __init__(self):
        self.items = []
        self.max_size = 5

    def get_items(self):
        return self.items

    # Add an element to the top of the stack
    def push(self, item):
        if self.length() >= self.max_size:
            raise OverflowError("Stack is full. Cannot push.")
        self.items.append(item)

    #  Remove the element from the top of the stack
    def pop(self):
        if self.length() == 0:
            raise IndexError("Stack is empty. Cannot pop.")
        return self.items.pop(-1)

    # View the element at the top of the stack without removing it
    def peek_head(self):
        print("The first item is: " + str(self.items[-1]))
        # raise IndexError("Cannot peek from an empty stack.")

    # Return the number of elements in the stack
    def length(self):
        return len(self.items)

    def __str__(self):
        return (
            "The stack size is: "
            + str(self.length())
            + "; Values: "
            + str(self.get_items())
        )


#  Implement a Circular Queue using an Array or List -- the last position (tail) connects back to the first (head).
class CircularQueue(Queue):
    pass


# run
q = Queue()
for i in range(1, 5):
    q.enqueue(i)
print(q)
q.enqueue(5)
# q.enqueue(5) <- overflow
q.dequeue()
print(q)
q.peek_head()
q.reverse()

print()

s = Stack()
for i in range(2, 10, 2):
    s.push(i)
print(s)
s.push(10)
# s.push(10) <- overflow
print(s)
s.pop()
print(s)
s.peek_head()
