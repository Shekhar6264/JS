class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod    
    def hascycle(head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
a = [3,2,1,4,5]
head = ListNode(a[0])
current = head
for i in range(1, len(a)):
    current.next = ListNode(a[i])
    current = current.next
current.next = head.next
result = ListNode.hascycle(head)
print("Does the linked list have a cycle? ", result)
