""" Doubly Linked List"""


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertNode(self, val, loc):

        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        # Insert at first
        elif loc == 0:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        # Insert at last
        elif loc == -1:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        # Insert at given location
        else:
            i = 0
            cur = self.head
            while i < loc - 1:
                cur = cur.next
                i += 1

            newNode.prev = cur
            newNode.next = cur.next
            cur.next = newNode

            if cur == self.tail:
                self.tail = newNode

    def deleteNode(self, loc):

        if self.head is None:
            return "In bound"

        else:
            if loc == 0:
                self.head = self.head.next
                self.head.prev = None

            elif loc == -1:
                self.tail.prev.next = None
                self.tail = self.tail.prev

            else:
                i = 0
                cur = self.head
                while i < loc - 1:
                    cur = cur.next
                    i += 1

                cur.next = cur.next.next
                cur.next.prev = cur

    # Reverse Doubly Linked List
    def reverseDLL(self):
        cur = self.head
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        self.head = prev

        cur = self.head
        cur_prev = None

        while cur:
            cur.prev = cur_prev
            cur_prev = cur
            cur = cur.next

    # Reverse Doubly Linked List with in a range
    def rangeReverse(self, left, right):

        l_prev, cur = None, self.head
        for _ in range(left - 1):
            l_prev, cur = cur, cur.next

        prev = None
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        l_prev.next.next = cur
        l_prev.next = prev
        cur = l_prev
        cur_prev = None
        while cur:
            cur.prev = cur_prev
            cur_prev = cur
            cur = cur.next

    # Search Doubly Linked List
    def searchNode(self, val):
        cur = self.head
        while cur:
            if cur.val == val:
                return cur.val
            cur = cur.next
        return "No val found"

    def traverse(self):
        cur = self.head
        while cur:
            print(
                "Current->",
                cur.val,
                "|",
                "Current Previous->",
                cur.prev.val if cur.prev else None,
                "|",
                "Current Next->",
                cur.next.val if cur.next else None,
            )
            cur = cur.next

    def deletionDLL(self):
        cur = self.head
        while cur:
            cur.prev = None
            cur = cur.next
        self.head = None
        self.tail = None


obj = DoublyLinkedList()
obj.insertNode(0, 0)
obj.insertNode(1, 1)
obj.insertNode(2, 2)
obj.insertNode(3, -1)

# obj.deleteNode(1)
# obj.reverseDLL()
obj.rangeReverse(2, 3)
obj.traverse()
