# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxProduct(self, root):
        dist = {}

        def dfs(node):

            if not node:
                return 0

            l = dfs(node.left)
            r = dfs(node.right)

            val = node.val + l + r
            dist[node] = val

            return val

        dfs(root)

        p = dist[root]
        res = 0
        for n, b in dist.items():
            if n != root:
                a = p - b
                res = max(res, a * b)

        return res % (10 ** 9 + 7)