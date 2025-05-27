# https://leetcode.com/problems/linked-list-cycle/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def hasCycle(head):
    
    slow, fast = head, head
    
    while fast and fast.next:
        
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
        
    return False


obj = ListNode(3)
obj.next = ListNode(2)
obj.next.next = ListNode(0)
obj.next.next.next = ListNode(-4)
obj.next.next.next.next = obj.next  # added a cycle
print(hasCycle(obj))  # Output: True