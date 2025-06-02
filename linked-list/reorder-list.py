# https://leetcode.com/problems/reorder-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        
        # Two pointer approach 2 x fast easily reach at last 
        slow, fast = head, head.next
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        
        # Reverse second half
        second_half = slow.next
        prev = slow.next = None
        while second_half:
            next = second_half.next
            second_half.next = prev
            prev = second_half
            second_half = next
            
            
        # Merge Two halfs
        first_half, second_half = head, prev
        while second_half:
            tmp1, tmp2 = first_half.next, second_half.next
            first_half.next = second_half   
            second_half.next = tmp1
            first_half, second_half = tmp1, tmp2 # recover here


obj = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(Solution().reorderList(obj))
