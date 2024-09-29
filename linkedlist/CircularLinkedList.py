""" Circular Linked List """


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class CircularLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data, loc=None):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            self.tail.next = self.head
        elif loc == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        elif loc == -1:
            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node
        else:
            cur = self.head
            for _ in range(loc - 1):
                cur = cur.next
            new_node.next = cur.next
            cur.next = new_node
            if cur == self.tail:
                self.tail = new_node

    def search(self, val):
        if not self.head:
            return "List is empty"
        cur = self.head
        while True:
            if cur.val == val:
                return cur.val
            if cur == self.tail:
                break
            cur = cur.next
        return "Value not found"

    def delete(self, loc):
        if self.head is None:
            return "List is empty"
        if loc == 0:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
        elif loc == -1:
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                cur = self.head
                while cur.next != self.tail:
                    cur = cur.next
                cur.next = self.head
                self.tail = cur
        else:
            cur = self.head
            for _ in range(loc - 1):
                cur = cur.next
            cur.next = cur.next.next

    def delete_entire(self):
        self.head = self.tail = None

    def reverse(self):
        if not self.head or self.head == self.tail:
            return
        prev, cur = None, self.head
        while True:
            nxt = cur.next
            cur.next = prev
            prev = cur
            if cur == self.tail:
                break
            cur = nxt
        self.head.next = prev
        self.head, self.tail = self.tail, self.head

    def range_reverse(self, left, right):
        if left == right:
            return
        l_prev, cur = None, self.head
        for _ in range(left - 1):
            l_prev, cur = cur, cur.next
        prev = None
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        if l_prev:
            l_prev.next.next = cur
            l_prev.next = prev
        else:
            self.head.next = cur
            self.head = prev

    def traverse(self):
        if not self.head:
            return
        cur = self.head
        while True:
            print(cur.val)
            if cur == self.tail:
                break
            cur = cur.next


# Example usage
obj = CircularLL()
obj.insert(0, 0)
obj.insert(1, 1)
obj.insert(2, 2)
obj.insert(3, 3)
obj.insert(4, -1)
obj.traverse()
