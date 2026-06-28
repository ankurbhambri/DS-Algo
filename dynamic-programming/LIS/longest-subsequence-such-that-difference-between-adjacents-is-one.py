# https://www.geeksforgeeks.org/dsa/longest-subsequence-such-that-difference-between-adjacents-is-one/

from bisect import bisect_left


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


# Variant: What if we need to find longest increasing sequence whose difference is 1.

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


# Variant: What if we need to find longest increasing sequence whose difference is atmost d.

# Segment tree (point update + range query) + Binary search

# TC: O(n log n)
# SC: O(n)
class Solution:
    def longest_sequence(self, arr, d):

        # Coordinate Compression kya karta hai

        # [1, 2, 3, 4, 5]  ← actual values

        # Index mapping:
        # 1 → 0
        # 2 → 1
        # 3 → 2
        # 4 → 3
        # 5 → 4

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
            
            # yeh nikalega ki x-d se chhota ya barabar ka last index kaha hai
            l = bisect_left(vals, x - d)

            # yeh dekhega ki x se chhota ya barabar ka last index kaha hai
            r = bisect_left(vals, x) - 1

            best = 0
            if l <= r:
                # yha pe hum query kar rahe hai ki l se r ke beech me maximum length kya hai
                best = query(1, 0, m - 1, l, r)

            # jo bhi best length hai usme 1 add kar do kyuki hum x ko bhi include kar rahe hai
            cur = best + 1

            # ab hum update kar rahe hai ki x ke liye maximum length kya hai
            update(1, 0, m - 1, r + 1, cur)

            ans = max(ans, cur)

        return ans


print(Solution().longest_sequence([1, 5, 2, 4, 3], 2)) # 3
print(Solution().longest_sequence([10, 1000000000, 15], 5)) # 2