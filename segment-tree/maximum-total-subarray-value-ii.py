# https://leetcode.com/problems/maximum-total-subarray-value-ii


from heapq import heappop, heappush


class SegmentTree:
    class Node:
        def __init__(self, start, end):
            self.start = start
            self.end = end
            self.mn = float("inf")
            self.mx = float("-inf")
            self.left = None
            self.right = None

    def __init__(self, nums):
        self.root = self._build(nums, 0, len(nums) - 1)

    def _build(self, nums, l, r):
        node = self.Node(l, r)

        if l == r:
            node.mn = nums[l]
            node.mx = nums[l]
            return node

        mid = (l + r) // 2

        node.left = self._build(nums, l, mid)
        node.right = self._build(nums, mid + 1, r)

        node.mn = min(node.left.mn, node.right.mn)
        node.mx = max(node.left.mx, node.right.mx)

        return node

    def query(self, l, r):
        return self._query(self.root, l, r)

    def _query(self, node, l, r):
        if not node:
            return float("inf"), float("-inf")

        if l <= node.start and node.end <= r:
            return node.mn, node.mx

        if node.end < l or r < node.start:
            return float("inf"), float("-inf")

        left_mn, left_mx = self._query(node.left, l, r)
        right_mn, right_mx = self._query(node.right, l, r)

        return (
            min(left_mn, right_mn),
            max(left_mx, right_mx)
        )


class Solution:
    def maxTotalValue(self, nums, k):
        n = len(nums)

        st = SegmentTree(nums)

        # max heap => use negative values
        pq = []

        for i in range(n):
            j = n - 1
            mn, mx = st.query(i, j)
            val = mx - mn

            heappush(pq, (-val, i, j))

        ans = 0

        while k:
            val, i, j = heappop(pq)
            val = -val

            ans += val

            j -= 1

            if i <= j:
                mn, mx = st.query(i, j)
                new_val = mx - mn

                heappush(pq, (-new_val, i, j))

            k -= 1

        return ans