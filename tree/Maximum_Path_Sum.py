# https://leetcode.com/problems/binary-tree-maximum-path-sum/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root):
    res = -float("inf")

    def helper(node):

        nonlocal res

        if not node:
            return 0

        l = max(helper(node.left), 0)
        r = max(helper(node.right), 0)

        res = max(res, node.val + l + r)

        return max(l, r) + node.val

    helper(root)
    return res


obj = TreeNode(1)
obj.left = TreeNode(2)
obj.right = TreeNode(3)
print(maxPathSum(obj))
