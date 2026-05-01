# https://leetcode.com/problems/n-ary-tree-postorder-traversal


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# TC: O(n)
# SC: O(h) where h is the height of the tree
class Solution:
    def postorder(self, root):
        
        res = []
        # If the root is None, return the empty list

        def helper(node):

            if node is None:
                return

            # Traverse all children first
            for child in node.children:
                helper(child)

            # Then add the node's value to the result
            res.append(node.val)

        helper(root)
        return res