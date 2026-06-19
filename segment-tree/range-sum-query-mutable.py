# https://leetcode.com/problems/range-sum-query-mutable/


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

# TC: O(log n) for both range update and point query operations
# SC: O(n) for the tree and lazy arrays
class NumArray:
    def __init__(self, nums: list[int]):

        n = len(nums)

        self.n = n

        self.tree = [0] * (4 * n)  # Segment tree array

        self.build(nums, 0, 0, n - 1)

    def build(self, nums, node, start, end):

        if start == end:
            self.tree[node] = nums[start]
            return

        mid = (start + end) // 2

        left_child = 2 * node + 1

        right_child = 2 * node + 2

        self.build(nums, left_child, start, mid)

        self.build(nums, right_child, mid + 1, end)

        self.tree[node] = self.tree[left_child] + self.tree[right_child]


    def update(self, idx, val):

        def _update(node, start, end, idx, val):

            if start == end:
                self.tree[node] = val
                return

            mid = (start + end) // 2

            left_child = 2 * node + 1

            right_child = 2 * node + 2

            if idx <= mid:
                _update(left_child, start, mid, idx, val)
            else:
                _update(right_child, mid + 1, end, idx, val)

            self.tree[node] = self.tree[left_child] + self.tree[right_child]

        _update(0, 0, self.n - 1, idx, val)


    def sumRange(self, left: int, right: int):

        def _query(node, start, end, l, r):

            if r < start or end < l:
                return 0

            if l <= start and end <= r:
                return self.tree[node]

            mid = (start + end) // 2

            left_child = 2 * node + 1

            right_child = 2 * node + 2

            left_sum = _query(left_child, start, mid, l, r)

            right_sum = _query(right_child, mid + 1, end, l, r)

            return left_sum + right_sum

        return _query(0, 0, self.n - 1, left, right)


# Another approach is to use Fenwick Tree (Binary Indexed Tree) which is more space efficient and easier to implement.

# TC: O(log n) for both range update and point query operations
# SC: O(n) for the tree array
class NumArray:
    def __init__(self, nums):

        self.n = len(nums)

        self.nums = nums

        self.bit = [0] * (self.n + 1)

        for i, x in enumerate(nums):
            self._add(i + 1, x)

    # range update function
    def _add(self, i, delta):

        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    # point update function
    def update(self, index, val):

        # Fenwick tree ko add karna hota h toh hum usse, kitna add karna h vo bta rhe h, with help of new_value - old_value
        delta = val - self.nums[index]

        self.nums[index] = val

        self._add(index + 1, delta)

    def query(self, i):

        res = 0

        while i > 0:
            res += self.bit[i]
            i -= i & -i

        return res


    def sumRange(self, left, right):
        return self.query(right + 1) - self.query(left)