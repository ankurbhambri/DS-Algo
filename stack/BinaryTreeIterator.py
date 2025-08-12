class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTreeIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left_branch(root)

    def _push_left_branch(self, node):
        """Push all left children to the stack."""
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        """Return the next smallest number in inorder traversal."""
        node = self.stack.pop()
        val = node.val
        if node.right:
            self._push_left_branch(node.right)
        return val

    def hasNext(self):
        """Return True if there are still nodes to process."""
        return len(self.stack) > 0



iterator = BinaryTreeIterator(
    Node(4, Node(2, Node(1), Node(3)), Node(6, Node(5), Node(7)))
)
while iterator.hasNext():
    print(iterator.next(), end=" ") # Output: 1 2 3 4 5 6 7
