# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(inorder, postorder):

    pos = inorder.index(postorder[-1]) if inorder else -1

    return (
        TreeNode(
            postorder[-1],
            buildTree(inorder[:pos], postorder[:pos]),
            buildTree(inorder[pos + 1 :], postorder[pos:-1]),
        )
        if pos > -1
        else None
    )


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
print(buildTree(inorder, postorder))
