# https://leetcode.com/problems/maximum-total-subarray-value-i



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

    def _build(self, nums, node, start, end):
        # Base case: Jab leaf node par ho
        if start == end:
            self.tree_min[node] = nums[start]
            self.tree_max[node] = nums[start]
            return

        mid = (start + end) // 2

        left_child = 2 * node + 1
        right_child = 2 * node + 2

        # Left aur Right subtrees build karo
        self._build(nums, left_child, start, mid)
        self._build(nums, right_child, mid + 1, end)

        # Parent node ko update karo
        self.tree_min[node] = min(self.tree_min[left_child], self.tree_min[right_child])
        self.tree_max[node] = max(self.tree_max[left_child], self.tree_max[right_child])

    def query(self, node, start, end, l, r):

        # 1. No overlap
        if end < l or start > r:
            return float("inf"), float("-inf")

        # 2. Complete overlap
        if l <= start and end <= r:
            return self.tree_min[node], self.tree_max[node]

        # 3. Partial overlap
        mid = (start + end) // 2

        left_child = 2 * node + 1

        right_child = 2 * node + 2

        left_mn, left_mx = self.query(left_child, start, mid, l, r)

        right_mn, right_mx = self.query(right_child, mid + 1, end, l, r)

        return min(left_mn, right_mn), max(left_mx, right_mx)


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
            # node, start, end, l, r
            mn, mx = st.query(0, 0, n - 1, i, j)
            val = mx - mn
            heappush(hp, (-val, i, j))

        # K elements nikaalo
        while k and hp:
            val, i, j = heappop(hp)
            val = -val
            ans += val

            j -= 1
            if i <= j:
                # node, start, end, l, r
                mn, mx = st.query(0, 0, n - 1, i, j)
                new_val = mx - mn
                heappush(hp, (-new_val, i, j))
            k -= 1

        return ans