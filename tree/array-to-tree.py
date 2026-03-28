class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(arr):

    if not arr:
        return None

    m = (len(arr)) // 2

    temp = TreeNode(arr[m])

    temp.left = sortedArrayToBST(arr[:m])
    temp.right = sortedArrayToBST(arr[m + 1 :])

    return temp


print(sortedArrayToBST([-10, -3, 0, 5, 9]))
