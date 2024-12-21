class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.min_value = float("inf")
        self.max_value = float("-inf")
        self.left = None
        self.right = None


class SegmentTree:
    def __init__(self, nums):
        """
        Initialize your segment tree here.
        """

        def createTree(nums, l, r):
            if l > r:
                return None

            node = Node(l, r)
            if l == r:  # Leaf node
                node.total = nums[l]
                node.min_value = nums[l]
                node.max_value = nums[l]
                return node

            mid = (l + r) // 2
            node.left = createTree(nums, l, mid)
            node.right = createTree(nums, mid + 1, r)

            node.min_value = min(node.left.min_value, node.right.min_value)
            node.max_value = max(node.left.max_value, node.right.max_value)

            return node

        self.root = createTree(nums, 0, len(nums) - 1)

    def update(self, i, val):
        """
        Update value at index `i` to `val`.
        :type i: int
        :type val: int
        """

        def updateVal(node, i, val):
            if node.start == node.end:  # Leaf node
                node.total = val
                node.min_value = val
                node.max_value = val
                return

            mid = (node.start + node.end) // 2
            if i <= mid:
                updateVal(node.left, i, val)
            else:
                updateVal(node.right, i, val)

            node.min_value = min(node.left.min_value, node.right.min_value)
            node.max_value = max(node.left.max_value, node.right.max_value)

        updateVal(self.root, i, val)

    def queryMin(self, i, j):
        """
        Min of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        """

        def rangeMin(node, i, j):
            if node.start == i and node.end == j:
                return node.min_value

            mid = (node.start + node.end) // 2
            if j <= mid:
                return rangeMin(node.left, i, j)
            elif i > mid:
                return rangeMin(node.right, i, j)
            else:
                return min(
                    rangeMin(node.left, i, mid), rangeMin(node.right, mid + 1, j)
                )

        return rangeMin(self.root, i, j)

    def queryMax(self, i, j):
        """
        Max of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        """

        def rangeMax(node, i, j):
            if node.start == i and node.end == j:
                return node.max_value

            mid = (node.start + node.end) // 2
            if j <= mid:
                return rangeMax(node.left, i, j)
            elif i > mid:
                return rangeMax(node.right, i, j)
            else:
                return max(
                    rangeMax(node.left, i, mid), rangeMax(node.right, mid + 1, j)
                )

        return rangeMax(self.root, i, j)


# Example Usage
nums = [2, 3, -1, -2, 4, 8, 10]
segTree = SegmentTree(nums)

print(segTree.queryMin(1, 4))  # Min of range [1, 4] -> -2
segTree.update(2, 10)  # Update index 2 to value 10
print(segTree.queryMax(0, 6))  # Max of range [0, 6] -> 10
