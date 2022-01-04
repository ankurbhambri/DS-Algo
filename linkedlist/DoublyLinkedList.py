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

        elif loc == 0:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode

        elif loc == -1:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

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
            return 'In bound'

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
    def reverse(self):
        cur = self.tail
        while cur != self.head:
            prev = cur.prev
            nxt = cur.next
            cur.prev = nxt

    # Search Doubly Linked List
    def searchNode(self, val):
        cur = self.head
        while cur:
            if cur.val == val:
                return cur.val
            cur = cur.next
        return 'No val found'

    def traverse(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next

    def deletionDLL(self):
        cur = self.head
        while cur:
            cur.prev = None
            cur = cur.next
        self.head = None
        self.tail = None


obj = DoublyLinkedList()
obj.insertNode(0,0)
obj.insertNode(3,-1)
obj.insertNode(1,1)
obj.insertNode(2,2)

obj.deleteNode(1)

obj.traverse()

            