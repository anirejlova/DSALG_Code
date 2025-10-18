# Implement a Queue using an Array/List:
class Queue:
    def __init__(self):
        self.items = [1, 2, 3]

    # Add an element to the tail (rear) of the queue
    def enqueue(self, item):
        print("Enqueue")
        self.items.append(item)
        print(self.items)

    # Remove the element from the head (front) of the queue
    def dequeue(self):
        print("Dequeue")
        if not len(self.items) == 0:
            self.items.pop(0)
            print(self.items)
        else:
            print("Queue is empty")

    #  View the element at the head of the queue without removing it
    def peek(self):
        print("Peek")
        if not len(self.items) == 0:
            print(self.items[0])
        else:
            print("Queue is empty")

    #  Return the number of elements in the queue
    def length(self):
        print("Length")
        print(len(self.items))


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
        print(len(self.items))


# run
q = Queue()
q.enqueue(4)
q.dequeue()
q.peek()
q.length()

s = Stack()
print("for loop for data input:")
for i in range(1, 5):
    s.push(i)
s.pop()
s.peek()
s.length()
