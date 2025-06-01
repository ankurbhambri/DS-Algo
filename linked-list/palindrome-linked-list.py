# https://leetcode.com/problems/palindrome-linked-list/description/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head):

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        cur = slow
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        left, right = head, prev
        while right:

            if left.val != right.val:
                return False

            left = left.next
            right = right.next

        return True


obj = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
print(Solution().isPalindrome(obj))  # True
obj = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1)))))
print(Solution().isPalindrome(obj))  # True
obj = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(Solution().isPalindrome(obj))  # False
obj = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
print(Solution().isPalindrome(obj))  # False
obj = ListNode(1, ListNode(2, ListNode(3, ListNode(2, ListNode(1, ListNode(0))))))
print(Solution().isPalindrome(obj))  # False