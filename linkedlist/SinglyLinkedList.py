class Node:

    def __init__(self, val=None):
        self.val = val
        self.next = None


class SLinkedList:

    def __init__(self):
        self.head = None # first of node
        self.tail = None # last of node

    def printLL(self):

        node = self.head
        while node:
            print(node.val)
            node = node.next

    def insertSLL(self, val, location):

        newNode = Node(val)

        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:

            if location == 0:
                newNode.next = self.head
                self.head = newNode

            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode

            else:
                cur = self.head
                index = 0

                while index < location - 1:
                    cur = cur.next
                    index += 1
                nextNode = cur.next
                cur.next = newNode
                newNode.next = nextNode
                if cur == self.tail:
                    self.tail=newNode

    # Traverse Singly Linked List
    def traverseSLL(self):

        if self.head is None:
            print("The Singly Linked List does not exist")
        else:
            node = self.head
            while node is not None:
                print(node.val)
                node = node.next

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
    def deleteNode(self, location):

        if self.head is None:
            print("The SLL does not exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                cur = self.head
                index = 0
                while index < location - 1:
                    cur = cur.next
                    index += 1
                nextNode = cur.next
                cur.next = nextNode.next

    # Delete entire SLL
    def deleteEntireSLL(self):
        if self.head is None:
            print("The SLL does not exist")
        else:
            self.head = None
            self.tail = None


obj = SLinkedList()
obj.insertSLL(1, 1)
obj.insertSLL(2, 1)
obj.insertSLL(3, 1)
obj.insertSLL(4, 1)
obj.insertSLL(0, 0)
obj.insertSLL(7, -1)
obj.insertSLL(5, 1)


obj.printLL()
obj.deleteEntireSLL()
obj.printLL()
