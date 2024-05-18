def maxHeight(root):

    def helper(node):

        if not node:
            return 0

        # to explore left and right nodes
        l = helper(node.left)
        r = helper(node.right)

        # formula for height only max of left and right height and +1 for the current node
        return max(l, r) + 1

    return helper(root)
