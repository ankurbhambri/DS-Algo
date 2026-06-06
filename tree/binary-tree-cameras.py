# https://leetcode.com/problems/binary-tree-cameras/


# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# here 1 means we have a camera at the current node, 
# 2 means the current node is covered by a child camera,
# and 0 means the current node is not covered by any camera.

# why 2 is used to indicate that the current node is covered by a child camera? 
# because if the current node is covered by a child camera, then we don't need to place a camera at the current node, 
# so we can return 2 to indicate that the current node is covered by a child camera.

class Solution:
    def minCameraCover(self, root):

        self.res = 0

        def dfs(node):

            if not node:
                return 2  # why 2 here? because if the node is null then we can consider it as covered by a child camera, so we return 2

            left = dfs(node.left)
            right = dfs(node.right)

            if left == 0 or right == 0: # 0 means the child node is not covered by any camera, so we need to place a camera at the current node
                self.res += 1
                return 1  # place camera

            if left == 1 or right == 1: # 1 means the child node has a camera, so the current node is covered by a child camera
                return 2

            return 0  # not covered

        if dfs(root) == 0: # if the root node is not covered by any camera, then we need to place a camera at the root node
            self.res += 1

        return self.res