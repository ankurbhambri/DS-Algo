# https://leetcode.com/problems/boundary-of-binary-tree/

def boundaryOfBinaryTree(root):
    if not root:
        return []

    def left_boundary(node):
        if node:
            if node.left or node.right:
                res.append(node.val)
            left_boundary(node.left if node.left else node.right)

    def right_boundary(node):
        if node:
            if node.right or node.left:
                right_boundary(node.right if node.right else node.left)
                res.append(node.val)

    def leaves(node):
        if node:
            if not node.left and not node.right:
                res.append(node.val)
            leaves(node.left)
            leaves(node.right)

    res = [root.val]
    left_boundary(root.left)
    leaves(root)
    right_boundary(root.right)

    return res

