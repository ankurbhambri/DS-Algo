# https://leetcode.com/problems/binary-tree-maximum-path-sum/

'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.
'''


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
