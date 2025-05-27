# https://leetcode.com/problems/sort-list/description/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sortList(head: Optional[ListNode]) -> Optional[ListNode]:

    def merge(left, right):
        # Create a dummy node for merged list
        dummy = ListNode(0)
        current = dummy

        # Compare and merge nodes
        while left and right:
            if left.val <= right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next
            current = current.next

        # Attach remaining nodes
        if left:
            current.next = left
        if right:
            current.next = right

        return dummy.next

    # Base case: if list is empty or has one node
    if not head or not head.next:
        return head

    # Step 1: Find middle node using slow-fast pointer
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Split the list into two halves
    second_half = slow.next
    slow.next = None

    # Step 2: Recursively sort both halves
    left = sortList(head)
    right = sortList(second_half)

    # Step 3: Merge the sorted halves
    return merge(left, right)

# LL: [4, 2, 1, 3]
head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
sorted_head = sortList(head)
current = sorted_head
while current:
    print(current.val, end=" -> ")
    current = current.next

print("None")  # Output: 1 -> 2 -> 3 -> 4 -> None
