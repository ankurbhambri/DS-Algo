"""
- Instead of immediately updating child nodes, the updates are stored in the lazy array/tree.
- When a node is queried, its pending updates are applied before proceeding.

- Without lazy propagation, updating a range of values would require traversing and updating all affected nodes, which can be slow.
- With lazy propagation, we mark the range to be updated and postpone the actual update until it is needed.
"""

# Here we are doing range update and range query.

# TC: O(log n) for both range update and point query operations
# SC: O(n) for the tree and lazy arrays
class LazySegmentTree:
    def __init__(self, nums):

        n = len(nums)
        self.n = n
        self.tree = [0] * (4 * n)  # Segment tree array
        self.lazy = [0] * (4 * n)  # Lazy propagation array
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


    def apply_lazy(self, node, start, end):

        # Update the current node
        self.tree[node] += (end - start + 1) * self.lazy[node]

        # If not a leaf node, propagate the update to children
        if start != end:
            self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[2 * node + 2] += self.lazy[node]

        # Clear the lazy value for the current node
        self.lazy[node] = 0


    def update(self, node, start, end, l, r, val):

        # Apply any pending updates
        if self.lazy[node] != 0:
            self.apply_lazy(node, start, end)

        # out of bounds
        if start > r or end < l:
            return

        # Total overlap
        if start >= l and end <= r:

            self.tree[node] += (end - start + 1) * val

            if start != end:
                self.lazy[2 * node + 1] += val
                self.lazy[2 * node + 2] += val

            return

        # Partial overlap
        mid = (start + end) // 2

        left_child = 2 * node + 1

        right_child = 2 * node + 2

        self.update(left_child, start, mid, l, r, val)

        self.update(right_child, mid + 1, end, l, r, val)

        self.tree[node] = self.tree[left_child] + self.tree[right_child]


    def query(self, node, start, end, l, r):

        # Apply any pending updates
        if self.lazy[node] != 0:
            self.apply_lazy(node, start, end)

        # out of bounds
        if start > r or end < l:
            return 0

        # Total overlap
        if start >= l and end <= r:
            return self.tree[node]

        # Partial overlap
        mid = (start + end) // 2

        left_child = 2 * node + 1

        right_child = 2 * node + 2

        left_sum = self.query(left_child, start, mid, l, r)

        right_sum = self.query(right_child, mid + 1, end, l, r)

        return left_sum + right_sum


# Example Usage
nums = [1, 2, 3, 4, 5]

segment_tree = LazySegmentTree(nums)

# Query sum of range [1, 3]
print("Initial sum [1, 3]:", segment_tree.query(0, 0, segment_tree.n - 1, 1, 3))  # Output: 9

# Update range [1, 3] by adding 10
segment_tree.update(0, 0, segment_tree.n - 1, 1, 3, 10)

# Query sum of range [1, 3] after update
print("Updated sum [1, 3]:", segment_tree.query(0, 0, segment_tree.n - 1, 1, 3))  # Output: 39

segment_tree.update(0, 0, segment_tree.n - 1, 0, 4, 5)

# Query sum of range [0, 4]
print("Sum [0, 4]:", segment_tree.query(0, 0, segment_tree.n - 1, 0, 4))  # Output: 70