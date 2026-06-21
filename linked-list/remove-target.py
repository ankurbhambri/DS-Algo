'''
Q1 — Remove First Occurrence of Target from a Doubly Linked List. Given the head of a doubly linked list and an integer target,
remove the first node whose value equals target. Return the (possibly new) head node.
'''

# TC: O(n) | SC: O(1)

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

def remove_node(head, target):
    curr = head
    while curr:
        if curr.val == target:
            # If removing head
            if curr.prev is None:
                head = curr.next
                if head:
                    head.prev = None
            else:
                curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
            break  # remove only first match
        curr = curr.next
    return head


'''
Q2 — Remove Multiple Targets (with Duplicates) from a Doubly Linked List

A list of target values, e.g. [2, 3, 3, 3, 1, 1]

Remove exactly as many occurrences of each number as appear in the target list.
If the target list has two 3s, remove exactly two nodes with value 3.
Return the new head.

'''
from collections import Counter

# TC: O(n) | SC: O(k) where k is number of unique targets
class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

def remove_multi_nodes(head, targets):

    to_remove = Counter(targets)
    curr = head

    while curr:
        if curr.val in to_remove and to_remove[curr.val] > 0:

            # Remove current node
            if curr.prev is None:  # head node
                head = curr.next
                if head:
                    head.prev = None

            else:
                curr.prev.next = curr.next
                if curr.next:
                    curr.next.prev = curr.prev

            to_remove[curr.val] -= 1

        curr = curr.next

    return head