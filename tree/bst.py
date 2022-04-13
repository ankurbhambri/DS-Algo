class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    # Inorder Successor in Binary Search Tree
    def getSuccessor(self, root, p):
        res = None
        while root:
            if p >= root.val:
                root = root.right
            elif p < root.val:
                res = root
                root = root.left
            else:
                break
        return res

    # In-order predecessor of the given node in the BST
    def inorderPredecessor(self, root, p):
        res = None
        while root:
            if p.val == root.val:
                root = root.left
            elif p.val < root.val:
                root = root.left
            elif p.val > root.val:
                res = root
                root = root.right
            else:
                break
        return res
