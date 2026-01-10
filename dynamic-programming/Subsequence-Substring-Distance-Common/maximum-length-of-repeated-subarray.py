# https://leetcode.com/problems/maximum-length-of-repeated-subarray/

class Solution:
    def findLength(self, nums1, nums2):

        res = 0

        m, n = len(nums1), len(nums2)

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if nums1[i - 1] == nums2[j - 1]:

                    dp[i][j] = 1 + dp[i - 1][j - 1]

                    res = max(res, dp[i][j])

        return res

print(Solution().findLength([0, 1, 1, 1, 1], [1, 0, 1, 0, 1]))  # 2
print(Solution().findLength([1, 2, 3, 2, 1], [3, 2, 1, 4, 7]))  # 3