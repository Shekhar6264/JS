class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    @staticmethod
    def isPalindrome(head):
        def reverse(head):
            curr = head
            prev = None
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev
        
        if not head or not head.next:
            return True
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head2 = reverse(slow.next)
        slow.next = None
        i, j = head, head2
        while j:
            if i.val != j.val:
                return False
            i = i.next
            j = j.next
        return True
a = [1,2,3,2,1]
head = Node(a[0])
current = head
for i in range(1, len(a)):
    current.next = Node(a[i])
    current = current.next
result = Node.isPalindrome(head)
print("Is the linked list a palindrome? ", result)