class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):

    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt

    # concise way
    # prev = None
    # while head:
    #     head.next, prev, head = prev, head, head.next

    return prev


obj = ListNode(1)
obj.next = ListNode(2)
obj.next.next = ListNode(3)
obj.next.next.next = ListNode(4)
obj.next.next.next.next = ListNode(5)
print(reverseList(obj))
