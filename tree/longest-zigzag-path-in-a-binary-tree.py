# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:

        self.ans = 0

        def dfs(node):

            if not node:
                return -1, -1

            left = dfs(node.left)
            right = dfs(node.right)

            # yha hume right path ka length lena hai kyuki hume zigzag path chahiye, 
            # to agar hum left path ka length lenge to wo zigzag path nahi hoga, to hume right path ka length lena hai
            left_path = left[1] + 1

            # yha hume left path ka length lena hai kyuki hume zigzag path chahiye, 
            # to agar hum right path ka length lenge to wo zigzag path nahi hoga, to hume left path ka length lena hai
            right_path = right[0] + 1

            self.ans = max(self.ans, left_path, right_path)

            return left_path, right_path

        dfs(root)
        return self.ans