class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
def middleNode(self, head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
