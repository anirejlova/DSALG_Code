# Implement a Queue using an Array/List:
class Queue:
    def __init__(self):
        self.items = [1,2,3]

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

# run
q = Queue()
q.enqueue(4)
q.dequeue()
q.peek()
q.length()