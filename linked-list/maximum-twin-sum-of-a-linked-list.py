# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def pairSum(head):

    slow, fast = head, head
    prev = None

    while fast and fast.next:
        fast = fast.next.next
        # reverse ll logic
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt
    
    res = float('-inf')
    while slow:
        res = max(res, slow.val + prev.val)
        slow = slow.next
        prev = prev.next

    return res

obj = ListNode(5)
obj.next = ListNode(4)
obj.next.next = ListNode(2)
obj.next.next.next = ListNode(1)
obj.next.next.next.next = ListNode(3)
obj.next.next.next.next.next = ListNode(6)
print(pairSum(obj))  # Output: 11