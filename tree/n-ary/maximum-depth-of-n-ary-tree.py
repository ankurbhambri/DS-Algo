# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root):

        if not root:
            return 0

        q = [root]
        level = []
        depth = 0

        while q:

            for node in q:

                for child in node.children:
                    level.append(child)

            q = level
            level = []
            depth += 1

        return depth