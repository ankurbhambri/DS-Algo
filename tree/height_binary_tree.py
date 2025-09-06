# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

def maxHeight(root):

    def helper(node):

        if not node:
            return 0

        # to explore left and right nodes
        l = helper(node.left)
        r = helper(node.right)

        # formula for height only max of left and right height and +1 for the current node
        return 1 + max(l, r)

    return helper(root)
