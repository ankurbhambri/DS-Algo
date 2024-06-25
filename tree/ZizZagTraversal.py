# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzagLevelOrder(root):

    if not root:
        return []

    q = [root]

    res = [[root.val]]

    level = []
    odd_flag = True

    while q:
        for node in q:
            if node.left:
                level.append(node.left)
            if node.right:
                level.append(node.right)

        if level:
            if odd_flag:
                res.append([j.val for j in level[::-1]])  # (right to left)
                odd_flag = False  # once done with the odd level, set the flag to False
            else:
                res.append([k.val for k in level])  # (left to right)
                odd_flag = True  # once done with the even level, set the flag to True

        q = level
        level = []

    return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(zigzagLevelOrder(root))  # [[3], [20, 9], [15, 7]]
