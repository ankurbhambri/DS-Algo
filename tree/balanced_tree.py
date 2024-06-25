# https://leetcode.com/problems/balanced-binary-tree/

# This code is similar to height of tree, but we also check if the subtrees are balanced or not.
# If left and right height difference is greater than 1 means unbalanced tree else balanced tree.


def isBalanced(root):

    def helper(node):

        if not node:
            return 0

        l = helper(node.left)
        r = helper(node.right)

        # if any of the subtrees is unbalanced, return -1
        if l == -1 or r == -1 or abs(l - r) > 1:
            return -1

        return max(l, r) + 1

    return helper(root) != -1
