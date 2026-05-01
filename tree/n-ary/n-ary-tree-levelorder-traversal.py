# 429. N-ary Tree Level Order Traversal
# https://leetcode.com/problems/n-ary-tree-level-order-traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

from collections import defaultdict


class Solution:
    def levelOrder(self, root):

        if not root:
            return []

        self.res = defaultdict(list)

        def helper(node, level):

            if not node:
                return

            for child in node.children:
                helper(child, level + 1)
                self.res[level].append(child.val)

        helper(root, 1)

        self.res[0].append(root.val)

        n = max(self.res.keys())

        return [self.res[i] for i in range(n + 1)]