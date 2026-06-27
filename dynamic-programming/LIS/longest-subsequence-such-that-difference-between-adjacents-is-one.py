# https://www.geeksforgeeks.org/dsa/longest-subsequence-such-that-difference-between-adjacents-is-one/


# TC: O(n)
# SC: O(n)
class Solution:
    def longestSubseq(self, arr):
        dp = {}
        ans = 0
        for x in arr:
            dp[x] = 1 + max(dp.get(x - 1, 0), dp.get(x + 1, 0))
            ans = max(ans, dp[x])
        return ans


print(Solution().longestSubseq([1, 2, 3, 4, 5])) # 5
print(Solution().longestSubseq([1, 2, 3, 4, 5, 6, 7, 8, 9])) # 9


# Variant: Find longest increasing sequence whose difference is 1

# This is a simple one

# TC: O(n)
# SC: O(n)
class Solution:
    def longestSubseq(self, arr):

        dp = {}

        ans = 0

        for x in arr:

            dp[x] = 1 + dp.get(x - 1, 0)

            ans = max(ans, dp[x])

        return ans


print(Solution().longestSubseq([1, 2, 3, 4, 5])) # 5
print(Solution().longestSubseq([1, 2, 3, 4, 5, 6, 7, 8, 9])) # 9


# Variant: Find longest increasing sequence whose difference is atmost d

# Segment tree (point update + range query) + Binary search

from bisect import bisect_left

class Solution:
    def longest_sequence(self, arr, d):

        vals = sorted(set(arr))
        m = len(vals)

        tree = [0] * (4 * m)

        def update(node, l, r, idx, val):

            if l == r:
                tree[node] = max(tree[node], val)
                return

            mid = (l + r) // 2

            left_child = node * 2

            right_child = node * 2 + 1

            if idx <= mid:
                update(left_child, l, mid, idx, val)
            else:
                update(right_child, mid + 1, r, idx, val)

            tree[node] = max(tree[left_child], tree[right_child])

        def query(node, start, end, l, r):

            if l > end or r < start:
                return 0

            if l <= start and end <= r:
                return tree[node]

            mid = (start + end) // 2

            left_child = node * 2

            right_child = node * 2 + 1

            return max(query(left_child, start, mid, l, r), query(right_child, mid + 1, end, l, r))

        ans = 0
        for x in arr:

            left = bisect_left(vals, x - d)

            right = bisect_left(vals, x) - 1

            best = 0
            if left <= right:
                best = query(1, 0, m - 1, left, right)

            cur = best + 1

            idx = bisect_left(vals, x)

            update(1, 0, m - 1, idx, cur)

            ans = max(ans, cur)

        return ans


print(Solution().longest_sequence([1, 5, 2, 4, 3], 2)) # 3