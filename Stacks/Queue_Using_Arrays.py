class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, num):
        self.queue.append(num)

    def dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            return None
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        return len(self.queue) == 0
q = Queue()
q.enqueue(61)
q.enqueue(50)
q.enqueue(38)
q.enqueue(40)
print(q.peek())
print(q.dequeue())
print(q.size())
print(q.isEmpty())