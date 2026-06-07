class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def pop(self):
        if self.head is None:
            return None
        val = self.head.data
        self.head = self.head.next
        return val

    def peek(self):
        if self.head is None:
            return None
        return self.head.data

    def isEmpty(self):
        return self.head is None

s = Stack()
s.push(61)
s.push(50)
s.push(38)
s.push(40)
print(s.peek())
print(s.pop())
print(s.isEmpty())