# https://leetcode.com/problems/min-stack/


class Node:
    def __init__(self, val, nxt = None):
        self.val = val
        self.next = nxt

class MinStack:

    def __init__(self):
        self.head = None
        self.min_val = None

    def push(self, val: int) -> None:

        if self.head is None:
            self.head = Node(val)
            self.min_val = Node(val)
    
        else:
            self.head = Node(val, self.head)

            if self.min_val.val >= val:
                self.min_val = Node(val, self.min_val)

    def pop(self) -> None:

        if self.head is None:
            return None

        val = self.head.val

        if self.min_val and self.min_val.val == val:
            self.min_val = self.min_val.next

        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.min_val.val



obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())  # Returns -3
obj.pop()          # Removes -3
print(obj.top())     # Returns 0
print(obj.getMin())  # Returns -2
obj.push(-1)
print(obj.getMin())  # Returns -2
obj.pop()          # Removes -1
print(obj.top())     # Returns 0
print(obj.getMin())  # Returns -2
