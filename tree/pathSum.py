def hasPathSum(root, targetSum):

    def helper(node, curSum):

        if not node:
            return False

        # add the current node value to the sum
        curSum += node.val

        # if it is a leaf node
        if not node.left and not node.right:
            return curSum == targetSum

        # explore left and right nodes
        l = helper(node.left, curSum)
        r = helper(node.right, curSum)

        return l or r  # if either is True, return True

    return helper(root, 0)
