""" Single Linked List"""


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None  # first of node
        self.tail = None  # last of node

    def insertSLL(self, val, loc):

        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            # Insert at first
            if loc == 0:
                newNode.next = self.head
                self.head = newNode
            # Insert at last
            elif loc == -1:
                self.tail.next = newNode
                self.tail = newNode
            # Insert at given location
            else:
                cur = self.head
                index = 0

                while index < loc - 1:
                    cur = cur.next
                    index += 1

                newNode.next = cur.next
                cur.next = newNode
                # In case cur is equeal to last node
                if cur == self.tail:
                    self.tail = newNode

    # Search for a node in Singly Linked List
    def searchSLL(self, nodeval):

        if self.head is None:
            return "The list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.val == nodeval:
                    return node.val
                node = node.next
            return "The val does not exist in this list"

    #  Delete a node from Singly Linked List
    def deleteNode(self, loc):

        if self.head is None:
            return "In bound"
        else:
            if loc == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif loc == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                cur = self.head
                index = 0
                while index < loc - 1:
                    cur = cur.next
                    index += 1
                cur.next = cur.next.next

    # Delete entire SLL
    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.head = None
            self.tail = None

    # Reverse Linked List
    def reverseLL(self):
        cur = self.head
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    # Reverse Doubly Linked List with in a range
    def rangeReverse(self, left, right):

        cur = self.head

        l_prev = None

        for _ in range(left - 1):
            l_prev, cur = cur, cur.next

        prev = None
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # last node in cur = 5
        l_prev.next.next = cur
        # prev = 4->3->2
        l_prev.next = prev

        return self.head

    # Traverse Linked List
    def traverse(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next

    # Remove Duplicacy
    def removeDuplicay(self):

        cur = self.head

        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next


obj = SinglyLinkedList()
obj.insertSLL(1, 0)
obj.insertSLL(2, 1)
obj.insertSLL(2, 2) # Duplicacy added
obj.insertSLL(3, 2)
obj.insertSLL(4, 3)
obj.insertSLL(5, 4)
obj.insertSLL(6, 5)
obj.insertSLL(7, 6)
obj.insertSLL(8, -1)

# obj.deleteNode(1)
# obj.printLL()
# obj.traverse()
# obj.deleteEntireSLL()
# obj.reverseLL()
# obj.rangeReverse(2, 5)
obj.removeDuplicay()
obj.traverse()
