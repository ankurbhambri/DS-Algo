# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):

        dummy = ListNode(0, head)
        l = dummy
        r = head

        while n > 0 and r:
            r = r.next
            n -= 1

        while r: # this will ho till last and 
            l = l.next
            r = r.next

        l.next = l.next.next

        return dummy.next


obj = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(Solution().removeNthFromEnd(obj, 2))  # Should remove the 4th node from the end, which is 4
