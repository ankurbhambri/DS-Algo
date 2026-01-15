"""
    The idea here is to build a segment tree. Each node stores the left and right
    endpoint of an interval and the sum of that interval and product of that interval. 
    All of the leaves will store elements of the array and each internal node will store sum of leaves under it.
    Creating the tree takes O(n) time. Query and updates are both O(log n).
"""

# Operation 	                    Time Complexity
# Building the Segment Tree	            O(n)
# Query (Range Min/Max/Sum)	          O(log n)
# Update (Point or Range)             O(log n)

# Segment Tree Space Complexity: O(n)

class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.total = 0
        self.product = 1
        self.left = None
        self.right = None


class NumArray(object):
    def __init__(self, nums):
        """
        Initialize your data structure here.
        :type nums: List[int]
        """

        def createTree(nums, l, r):
            # Base case
            if l > r:
                return None

            # Leaf node
            if l == r:
                node = Node(l, r)
                node.total = nums[l]
                node.product = nums[l]
                return node

            # Internal node
            mid = (l + r) // 2
            root = Node(l, r)

            root.left = createTree(nums, l, mid)
            root.right = createTree(nums, mid + 1, r)

            root.total = root.left.total + root.right.total
            root.product = root.left.product * root.right.product
            return root

        self.root = createTree(nums, 0, len(nums) - 1)

    def update(self, i, val):
        """
        Update value at index `i` to `val`.
        :type i: int
        :type val: int
        """

        def updateVal(root, i, val):
            if root.start == root.end:
                root.total = val
                root.product = val
                return val

            mid = (root.start + root.end) // 2

            if i <= mid:
                updateVal(root.left, i, val)
            else:
                updateVal(root.right, i, val)

            root.total = root.left.total + root.right.total
            root.product = root.left.product * root.right.product

            return root.total, root.product

        return updateVal(self.root, i, val)

    def sumRange(self, i, j):
        """
        Sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        """

        def rangeSum(root, i, j):
            if root.start == i and root.end == j:
                return root.total

            mid = (root.start + root.end) // 2

            if j <= mid:
                return rangeSum(root.left, i, j)
            elif i > mid:
                return rangeSum(root.right, i, j)
            else:
                return rangeSum(root.left, i, mid) + rangeSum(root.right, mid + 1, j)

        return rangeSum(self.root, i, j)

    def productRange(self, i, j):
        """
        Product of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        """
        MOD = 10**9 + 7  # To handle overflow

        def rangeProduct(root, i, j):
            if root.start == i and root.end == j:
                return root.product % MOD

            mid = (root.start + root.end) // 2

            if j <= mid:
                return rangeProduct(root.left, i, j) % MOD
            elif i > mid:
                return rangeProduct(root.right, i, j) % MOD
            else:
                left_product = rangeProduct(root.left, i, mid)
                right_product = rangeProduct(root.right, mid + 1, j)
                return (left_product * right_product) % MOD

        return rangeProduct(self.root, i, j)


# Example Usage
numArray = NumArray([2, 3, -1, -2, 4, 8, 10])
print("Sum Range [0, 2]:", numArray.sumRange(0, 2))  # Output: 4
numArray.update(2, 10)
print("Updated Tree Total:", numArray.root.total)  # Output: Total sum of all nodes
print("Sum Range [0, 2]:", numArray.sumRange(0, 2))  # Output: 15
print("Product Range [0, 2]:", numArray.productRange(0, 2))  # Output: 60
