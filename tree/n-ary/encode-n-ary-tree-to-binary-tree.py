# https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/
# similar - https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/


class Node:
    def __init__(self, val = None, children = None):
        self.val = val
        self.children = children if children is not None else []

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root):

        if not root:
            return None

        node = TreeNode(root.val)

        if root.children:
            node.left = self.encode(root.children[0])

        curr = node.left

        for i in range(1, len(root.children)):
            curr.right = self.encode(root.children[i])
            curr = curr.right

        return node

	# Decodes your binary tree to an n-ary tree.
    def decode(self, root): # 'Optional[TreeNode]') -> 'Optional[Node]':

        if not root:
            return None

        node = Node(root.val, [])

        curr = root.left

        while curr:
            node.children.append(self.decode(curr))
            curr = curr.right

        return node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))