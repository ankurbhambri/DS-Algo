# https://leetcode.com/problems/unique-binary-search-trees-ii/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int):
        if n == 0:
            return []
        return self.build(1, n)

    def build(self, start, end):

        if start > end:
            return [None]

        all_trees = []

        for root_val in range(start, end + 1):
            left_trees = self.build(start, root_val - 1)
            right_trees = self.build(root_val + 1, end)
            
            for left in left_trees:
                for right in right_trees:
                    root = TreeNode(root_val)
                    root.left = left
                    root.right = right
                    all_trees.append(root)

        return all_trees