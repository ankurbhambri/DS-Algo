# https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

class Solution:
    def minDeletionSize(self, A: list[str]) -> int:

        n = len(A[0])
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):

                if all(a[j] <= a[i] for a in A):
                    dp[i] = max(dp[i], dp[j] + 1)

        return n - max(dp)

print(Solution().minDeletionSize(["babca","bbazb"]))  # Output: 3