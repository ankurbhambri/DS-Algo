# https://leetcode.com/problems/maximum-total-subarray-value-ii


from heapq import heappop, heappush

class SegmentTree:
    def __init__(self, nums):

        self.n = len(nums)

        # 4 * n size ke arrays min aur max store karne ke liye
        self.tree_min = [float("inf")] * (4 * self.n)
        self.tree_max = [float("-inf")] * (4 * self.n)

        if self.n > 0:
            self._build(nums, 0, 0, self.n - 1)

    def _build(self, nums, tree_idx, l, r):

        # Base case: Jab leaf node par ho
        if l == r:
            self.tree_min[tree_idx] = nums[l]
            self.tree_max[tree_idx] = nums[l]
            return

        mid = (l + r) // 2

        left_child = 2 * tree_idx + 1
        right_child = 2 * tree_idx + 2

        # Left aur Right subtrees build karo
        self._build(nums, left_child, l, mid)
        self._build(nums, right_child, mid + 1, r)

        # Parent node ko update karo
        self.tree_min[tree_idx] = min(self.tree_min[left_child], self.tree_min[right_child])
        self.tree_max[tree_idx] = max(self.tree_max[left_child], self.tree_max[right_child])

    def query(self, ql, qr):
        # Helper function range query ke liye
        def _query(tree_idx, l, r, ql, qr):
            # 1. No overlap
            if r < ql or l > qr:
                return float("inf"), float("-inf")
            
            # 2. Complete overlap
            if ql <= l and r <= qr:
                return self.tree_min[tree_idx], self.tree_max[tree_idx]

            # 3. Partial overlap
            mid = (l + r) // 2
            left_mn, left_mx = _query(2 * tree_idx + 1, l, mid, ql, qr)
            right_mn, right_mx = _query(2 * tree_idx + 2, mid + 1, r, ql, qr)

            return min(left_mn, right_mn), max(left_mx, right_mx)

        return _query(0, 0, self.n - 1, ql, qr)


class Solution:
    def maxTotalValue(self, nums, k):
        ans = 0
        n = len(nums)
        if n == 0:
            return 0
            
        st = SegmentTree(nums)
        hp = []

        # Heap ko initialize karo
        for i in range(n):
            j = n - 1
            mn, mx = st.query(i, j)
            val = mx - mn
            heappush(hp, (-val, i, j))

        # K elements nikaalo
        while k and hp:
            val, i, j = heappop(hp)
            val = -val
            ans += val

            j -= 1
            if i <= j:
                mn, mx = st.query(i, j)
                new_val = mx - mn
                heappush(hp, (-new_val, i, j))
            k -= 1

        return ans