
# https://leetcode.com/problems/intersection-of-two-linked-lists/


# Similar approach is used in finding the - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        l1, l2 = headA, headB
        
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1


obj = ListNode(1)
obj.next = ListNode(2)
obj.next.next = ListNode(3)
obj.next.next.next = ListNode(4)
obj2 = ListNode(5)
obj2.next = ListNode(6)
obj2.next.next = obj.next  # Intersection at node with value 3

print(Solution().getIntersectionNode(obj, obj2))
