# Min Stack O(1) operations


class Node:
    def __init__(self, val=None, nxt=None):
        self.val = val
        self.nxt = nxt


class MinStack:
    def __init__(self):
        self.topNode = None
        self.minVal = None

    def push(self, val: int) -> None:

        if self.topNode is None:
            self.topNode = Node(val=val)
            self.minVal = Node(val=val)

        else:

            if self.minVal.val >= val:
                self.minVal = Node(val=val, nxt=self.minVal)

            self.topNode = Node(val=val, nxt=self.topNode)

    def pop(self) -> None:

        if self.topNode is None:
            return None

        val = self.topNode.val

        if self.minVal and val == self.minVal.val:
            self.minVal = self.minVal.nxt

        self.topNode = self.topNode.nxt

    def top(self) -> int:
        print(self.topNode.val)
        return self.topNode.val

    def getMin(self) -> int:
        print(self.minVal.val)
        return self.minVal.val


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
obj.pop()
obj.top()
obj.getMin()
