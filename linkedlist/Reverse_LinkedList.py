class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printLinkedList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next


# https://leetcode.com/problems/reverse-linked-list/


def reverseList(head):

    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt

    # more concise way
    # prev = None
    # while head:
    #     head.next, prev, head = prev, head, head.next

    return prev


obj = ListNode(1)
obj.next = ListNode(2)
obj.next.next = ListNode(3)
obj.next.next.next = ListNode(4)
obj.next.next.next.next = ListNode(5)

printLinkedList(reverseList(obj))
print()


# Another question is to reverse a linked list from a certain position.
# https://www.interviewquery.com/questions/reverse-at-kth-position?utm_source=youtube&utm_medium=social


def reverse_at_position(head, position):
    if head is None or position == 0:
        return head

    curr = head

    # Move curr to the node just before the specified position
    while position > 1 and curr:
        position -= 1
        curr = curr.next

    # If position is beyond the list or no node to reverse after curr, return head
    if curr is None or curr.next is None:
        return head

    new_curr = curr.next
    curr.next = None
    prev = None

    # Reverse the sublist starting from new_curr
    while new_curr:
        nxt = new_curr.next
        new_curr.next = prev
        prev = new_curr
        new_curr = nxt

    # Connect the reversed sublist back to the main list
    curr.next = prev

    return head


obj = ListNode(1)
obj.next = ListNode(2)
obj.next.next = ListNode(3)
obj.next.next.next = ListNode(4)
obj.next.next.next.next = ListNode(5)

printLinkedList(reverse_at_position(obj, 2))  # 1 -> 4 -> 3 -> 2 -> 5
