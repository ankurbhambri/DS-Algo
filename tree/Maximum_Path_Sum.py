# https://leetcode.com/problems/binary-tree-maximum-path-sum/

def solution():
    res = -float("inf")

    def helper(node):

        nonlocal res

        if not node:
            return 0

        l = max(helper(node.left), 0)
        r = max(helper(node.right), 0)

        res = max(self.res, node.val + l + r)

        return max(l, r) + node.val

    helper(root)
    return res
