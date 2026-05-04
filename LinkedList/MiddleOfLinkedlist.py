class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
def middleNode(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
a = [1,2,3,4,5]
head = Node(a[0])
current = head
for i in range(1, len(a)):
    current.next = Node(a[i])
    current = current.next
result = middleNode(head)
print("Middle node value: ", result.val)