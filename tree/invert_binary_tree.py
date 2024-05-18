def invertTree(root):

    def helper(node):

        if not node:
            return

        l = helper(node.left)
        r = helper(node.right)

        node.left = r
        node.right = l

        return node

    return helper(root)
