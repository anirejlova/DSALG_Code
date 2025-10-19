class Queue:
    def __init__(self):
        self.data = []
        self.head = 0
        self.tail = -1
        self.max_size = 15

    def enqueue(self, newData):
        print("Enqueue the data " + str(newData))
        if self.tail == self.max_size - 1:
            raise OverflowError("Cannot insert into a full queue.")
        self.tail += 1
        self.data.insert(self.tail, newData)
        print("Now the tail index is " + str(self.tail))

    def dequeue(self):
        if self.tail == -1:
            raise IndexError("Cannot delete from an empty queue.")
        removed = self.data[self.head]
        print("Dequeue the data " + str(removed))
        temp = self.head
        while temp < self.tail:
            temp += 1
            self.data[temp - 1] = self.data[temp]
        del self.data[temp]
        self.tail -= 1
        return removed

    def peek(self):
        if self.tail == -1:
            raise IndexError("Cannot peek from an empty queue.")
        print("Peek the head")
        return self.data[self.head]

    def length(self):
        return self.tail + 1

    def print_message(self):
        print(
            "The queue size is "
            + str(self.length())
            + " The first element is "
            + str(self.peek())
        )

    def print_all(self):
        while self.tail != -1:
            print(self.dequeue())

    def reverse(self):
        print("\nBefore reverse, the queue is ", self.data)
        stack = Stack()
        while self.length() > 0:
            element = self.dequeue()
            stack.push(element)
        while stack.length() > 0:
            element = stack.pop()
            self.enqueue(element)
        print("\nThe reversed queue is ", self.data)


class Stack:
    def __init__(self):
        self.data = []
        self.top = -1
        self.max_size = 5

    def push(self, newData):
        print("Push the data " + str(newData))
        if self.top == self.max_size - 1:
            raise OverflowError("Cannot insert into a full stack.")
        self.top += 1
        self.data.insert(self.top, newData)
        print("Now the top index is " + str(self.top))

    def pop(self):
        if self.top == -1:
            raise IndexError("Cannot delete from an empty stack.")
        removed = self.data[self.top]
        del self.data[self.top]
        self.top -= 1
        print("Pop the data " + str(removed))
        return removed

    def peek(self):
        if self.top == -1:
            raise IndexError("Cannot peek from an empty stack.")
        print("Peek the top")
        return self.data[self.top]

    def length(self):
        return self.top + 1

    def print_message(self):
        print(
            "The stack size is "
            + str(self.length())
            + " The top element is "
            + str(self.peek())
        )

    def print_all(self):
        while self.top != -1:
            print(self.pop())


# run
print("Queue operations:")
q = Queue()
for j in range(10, 20):
    q.enqueue(50 - j)

q.print_message()
for i in range(10, 16):
    q.dequeue()

q.print_message()
q.print_all()

print()
print("\nReverse Queue:")
q2 = Queue()
for i in range(0, 5):
    q2.enqueue(i)
q2.reverse()

print()
print("Stack operations:")
s = Stack()
for i in range(1, 9):  # raised OverflowError on 6th push <- full stack
    s.push(i)

s.print_message()
for i in range(1, 5):  # raised IndexError on 4th pop <- empty stack
    s.pop()

s.print_message()
s.print_all()
