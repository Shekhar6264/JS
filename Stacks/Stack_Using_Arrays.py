class Stack:
    def __init__(self):
        self.stack = []

    def push(self, num):
        self.stack.append(num)

    def pop(self):
        if self.isEmpty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.isEmpty():
            return None
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def isEmpty(self):
        return len(self.stack) == 0
s = Stack()
s.push(61)
s.push(50)
s.push(38)
s.push(40)
print(s.peek())
print(s.pop())
print(s.size())
print(s.isEmpty())