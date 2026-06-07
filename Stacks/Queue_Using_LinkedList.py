class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        newNode = Node(data)
        if self.tail is None:
            self.head = self.tail = newNode
            return
        self.tail.next = newNode
        self.tail = newNode

    def dequeue(self):
        if self.head is None:
            return None
        val = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return val

    def peek(self):
        if self.head is None:
            return None
        return self.head.data

    def isEmpty(self):
        return self.head is None
    
q = Queue()
q.enqueue(61)
q.enqueue(50)
q.enqueue(38)
q.enqueue(40)
print(q.peek())
print(q.dequeue())
print(q.isEmpty())