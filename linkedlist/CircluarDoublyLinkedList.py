''' Circluar Doubly Linked List'''


class Node:
     def __init__(self, val=None, next=None, prev=None):
         self.val = val
         self.next = next
         self.prev = prev


class CircularDoublyLL:

    def __init__(self):
        self.head = None
        self.tail = None

    def insertNode(self, val, loc):

        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            # Insert at first
            if loc == 0:

                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode

                self.tail.next = self.head
                self.head.prev = self.tail

            # Insert at last
            elif loc == -1:
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode

                newNode.next = self.head
                self.head.prev = newNode

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

    # Traverse linked list
    def traverse(self):
        cur = self.head
        while cur:
            print(
                "Current->",cur.val,
                '|',
                "Current Previous->", cur.prev.val if cur.prev else None,
                '|',
                "Current Next->",cur.next.val if cur.next else None
            )
            if cur.next == self.head:
                break
            cur = cur.next

    def deleteNode(self, loc):
        if self.head is None:
            return 'In bound'

        else:
            if loc == 0:

                nxt = self.head.next
                self.tail.next = nxt
                nxt.prev = self.tail
                self.head = nxt

            elif loc == -1:
                prev = self.tail.prev
                prev.next = self.head
                self.head.prev = prev
                self.tail = prev     
           
            else:
                cur = self.head
                i = 0
                while i < loc - 1:
                    cur = cur.next
                    i += 1

                cur.next = cur.next.next
                cur.next.prev = cur


    # Reverse Circular Doubly Linked List
    def reverseCDLL(self):
        cur = self.head
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            if cur == self.tail:
                nxt.next = prev
                self.head = prev
                self.tail = nxt
                break
            cur = nxt

        self.head = prev

        cur = self.head
        cur_prev = None
        while cur:
            cur.prev = cur_prev
            cur_prev = cur
            if cur == self.tail:
                self.head.prev = self.tail
                self.tail.next = self.head
                break
            cur = cur.next

    # Reverse Circular Doubly Linked List with in a range
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
        cur_prev = self.head.prev

        while cur:
            cur.prev = cur_prev
            cur_prev = cur
            if cur == self.tail:
                self.head.prev = self.tail
                self.tail.next = self.head
                break
            cur = cur.next


    # Search Circular Doubly Linked List
    def searchNode(self, val):
        cur = self.head
        while cur:
            if cur.val == val:
                return cur.val
            if cur == self.tail:
                return 'No value found'
            cur = cur.next
        return 'No val found'

obj = CircularDoublyLL()
obj.insertNode(0,0)
obj.insertNode(1,1)
obj.insertNode(2,2)
obj.insertNode(3,-1)

# obj.deleteNode(3)
# obj.reverseCDLL()
obj.rangeReverse(2,3)
obj.traverse()
