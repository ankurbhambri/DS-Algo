class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class CircularLL:

    def __init__(self):
        self.head = None # first of node
        self.tail = None # last of node

    def insertCll(self, data, loc=None):

        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            self.tail.next = self.head

        elif loc == 0:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = self.head

        elif loc == -1:
            newNode.next = self.tail.next # or self.head basically this is head node
            self.tail.next = newNode
            self.tail = newNode

        else:
            cur = self.head
            i = 0
            while i < loc - 1:
                cur = cur.next
                i += 1
            
            nextNode = cur.next
            cur.next = newNode
            newNode.next = nextNode

            if cur == self.tail:
                self.tail = newNode

    def searchnode(self, val):

        if not self.node:
            return 'In bound'

        elif val is not None:
            cur = self.head
            while cur:
                if cur.val == val:
                    return cur.val
                cur = cur.next

        return "The val does not exist in this list"

    def deletenode(self, loc):

        if self.head is None:
            return 'In bound'

        elif loc == 0:
            self.head = self.head.next
            self.tail.next = self.head

        elif loc == -1:
            prev = None
            cur = self.head
            while cur != self.tail:
                prev = cur 
                cur = cur.next
            self.tail = prev
            self.tail.next = self.head

        else:
            i = 0
            cur = self.head
            while i < loc - 1:
                cur = cur.next
                i += 1

            cur.next = cur.next.next

    def deleteEntire(self):

        self.head = None
        self.tail.next = None
        self.tail = None

    # Reverse Circular Linked List
    def reverseLL(self):

        cur = self.head
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            if cur == self.tail:
                # prev = self.tail and nxt = self.head so nxt.next is prev
                nxt.next = prev
                self.head = prev
                self.tail = nxt
                return prev
            cur = nxt

    # Traverse Linked List
    def traverse(self):
        cur = self.head
        while cur and cur != self.tail:
            print(cur.val)
            cur = cur.next
        print(cur.val)


# 0 means start 1 means add after first and -1 means add at last

obj = CircularLL()

obj.insertCll(0, 0)
obj.insertCll(1, 1)
obj.insertCll(2, 2)
obj.insertCll(3, 3)
obj.insertCll(4, -1)

# provide +1 in location coz we have 1 decrement
# obj.deletenode(1) 
obj.reverseLL()
obj.traverse()
