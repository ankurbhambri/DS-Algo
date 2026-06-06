# https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/

# TC: O(n^2 Log m), where m is the max(A)
# SC: O(n)
class Solution:
    def lenLongestFibSubseq(self, A):

        res = 2
        s = set(A)

        for i in range(len(A)):
            for j in range(i + 1, len(A)):

                a, b, l = A[i], A[j], 2
                while a + b in s:
                    a, b, l = b, a + b, l + 1
                res = max(res, l)
        return res if res > 2 else 0

print(Solution().lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))

# Optimised version

# TC: O(n^2)
# SC: O(n^2)
class Solution:
    def lenLongestFibSubseq(self, arr):

        dp = {}
        index = {x: i for i, x in enumerate(arr)}
        max_len = 0
        n = len(arr)

        for i in range(n):
            for j in range(i):

                # We want arr[k] + arr[i] == arr[j] -> arr[k] = arr[j] - arr[i]
                target = arr[i] - arr[j]

                if target in index and index[target] < j:

                    k = index[target]
                    # If dp[k][i] doesn't exist, the base length is 2 (arr[k] and arr[i])
                    # Adding arr[j] makes it 2 + 1 = 3
                    dp[j, i] = dp.get((k, j), 2) + 1

                    max_len = max(max_len, dp[j, i])

        return max_len if max_len >= 3 else 0

print(Solution().lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))