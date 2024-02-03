# https://leetcode.com/problems/invert-binary-tree/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root):

    def helper(node):

        if not node:
            return

        l = helper(node.left)
        r = helper(node.right)

        node.left = r
        node.right = l

        return node

    return helper(root)


obj = TreeNode(4)
obj.left = TreeNode(2)
obj.right = TreeNode(7)
obj.left.left = TreeNode(1)
obj.left.right = TreeNode(3)
obj.right.left = TreeNode(6)
obj.right.right = TreeNode(9)
print(invertTree(obj))
