# https://leetcode.com/problems/binary-tree-maximum-path-sum/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root):

        self.res = float("-inf")

        def helper(node):

            if not node:
                return 0

            l = max(0, helper(node.left))
            r = max(0, helper(node.right))

            self.res = max(self.res, node.val + l + r)

            return node.val + max(l, r)

        helper(root)
        return self.res


obj = TreeNode(1)
obj.left = TreeNode(2)
obj.right = TreeNode(3)
print(Solution().maxPathSum(obj))
