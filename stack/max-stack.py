# Max Stack O(1) operations


class Node:
    def __init__(self, val=None, nxt=None, prev=None):
        self.val = val
        self.nxt = nxt
        self.prev = prev


class MaxStack:
    def __init__(self):
        self.head = None
        self.maxNode = None

    """
    @param: number: An integer
    @return: nothing
    """

    def push(self, val):

        newNode = Node(val=val)

        if self.head is None:
            self.head = newNode
            self.maxNode = newNode
        else:
            if self.maxNode.val <= val:
                self.maxNode = Node(val=val, nxt=self.maxNode)

            newNode.nxt = self.head
            self.head.prev = newNode
            self.head = newNode

    """
    @return: An integer
    """

    def pop(self):
        if self.head is None:
            return None
        else:
            val = self.head.val
            if self.maxNode and val == self.maxNode.val:
                self.maxNode = self.maxNode.nxt
            self.head = self.head.nxt
            return val

    """
    @return: An integer
    """

    def top(self):
        print(self.head.val)
        return self.head.val

    """
    @return: An integer
    """

    def peekMax(self):
        return self.maxNode.val

    """
    @return: An integer
    """

    def popMax(self):
        if self.maxNode is None:
            return None
        else:
            val = self.maxNode.val
            if self.head and val == self.head.val:
                self.head = self.head.nxt
            else:
                cur = self.head
                while cur:
                    if cur.val == val:
                        pv, nt = cur.prev, cur.nxt
                        if nt:
                            pv.nxt = nt
                            nt.prev = pv
                        self.maxNode.nxt = self.maxNode
                        return val
                    cur = cur.nxt

            self.maxNode.nxt = self.maxNode
            return val

    def llpeek(self):
        cur = self.head
        while cur:
            cur = cur.nxt
