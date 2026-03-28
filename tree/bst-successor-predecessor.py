class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderSuccessor(root: TreeNode, p: TreeNode) -> TreeNode:
    successor = None
    
    while root:
        if p.val < root.val:
            successor = root  # Potential successor
            root = root.left
        else:
            root = root.right
    
    return successor

def inorderPredecessor(root: TreeNode, p: TreeNode) -> TreeNode:
    predecessor = None

    while root:
        if p.val > root.val:
            predecessor = root  # Potential predecessor
            root = root.right
        else:
            root = root.left

    return predecessor

def inorderTraversal(root):

    res = []

    def helper(node):

        if node:

            helper(node.left)

            res.append(node.val)

            helper(node.right)

    helper(root)

    return res

print(inorderTraversal(TreeNode(20, TreeNode(10, None, TreeNode(15)))))  # [10, 15, 20]

print(inorderSuccessor(TreeNode(20, TreeNode(10, None, TreeNode(15)), TreeNode(30)), TreeNode(15)).val)  # 20

print(inorderPredecessor(TreeNode(20, TreeNode(10, None, TreeNode(15)), TreeNode(30)), TreeNode(15)).val)  # 10
