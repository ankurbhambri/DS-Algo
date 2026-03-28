# https://leetcode.com/problems/balance-a-binary-search-tree/


# Idea behind the solution is to first do inorder traversal of the tree and store the values in an array.
# Then binary partitioning the array to create a balanced binary tree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def balanceBST(root):

    arr = []

    def inorder(node):
        if node:
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)

    def createBinaryTree(l, h):

        if l > h:
            return None

        m = (l + h) // 2  # binary partitioning

        node = TreeNode(arr[m])

        node.left = createBinaryTree(l, m - 1)

        node.right = createBinaryTree(m + 1, h)

        return node

    inorder(root)
    return createBinaryTree(0, len(arr) - 1)


obj = TreeNode(1)
obj.right = TreeNode(2)
obj.right.right = TreeNode(3)
obj.right.right.right = TreeNode(4)
print(balanceBST(obj))
