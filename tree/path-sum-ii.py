# https://leetcode.com/problems/path-sum-ii/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root, target):

        res = []

        def dfs(node, path, total):

            if not node:
                return

            if(total + node.val == target and not node.left and not node.right):
                res.append(path + [node.val])
                return

            if(node.left):
                dfs(node.left, path + [node.val], total + node.val)

            if(node.right):
                dfs(node.right, path + [node.val], total + node.val)

        dfs(root, [], 0)

        return res