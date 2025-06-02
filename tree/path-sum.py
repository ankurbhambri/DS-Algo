# https://leetcode.com/problems/path-sum/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root, targetSum):

    def helper(node, curSum):

        if not node:
            return False

        # add the current node value to the sum
        curSum += node.val

        # if it is a leaf node means no other left or right child.
        if not node.left and not node.right:
            return curSum == targetSum

        # explore left and right nodes
        l = helper(node.left, curSum)
        r = helper(node.right, curSum)

        return l or r  # if either side is True, return True

    return helper(root, 0)


obj = TreeNode(5)
obj.left = TreeNode(4)
obj.right = TreeNode(8)
obj.left.left = TreeNode(11)
obj.left.left.left = TreeNode(7)
obj.left.left.right = TreeNode(2)
obj.right.left = TreeNode(13)
obj.right.right = TreeNode(4)
obj.right.right.right = TreeNode(1)
print(hasPathSum(obj, 22))
