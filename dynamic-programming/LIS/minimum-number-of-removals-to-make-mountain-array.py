# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/


# TC: O(n^2)
# SC: O(n)
class Solution:
    def minimumMountainRemovals(self, nums):

        n = len(nums)

        def helper(arr):
            dp = [1] * n
            for i in range(n):
                for j in range(i):
                    if arr[i] > arr[j]:
                        dp[i] = max(dp[i], dp[j] + 1)
            return dp

        left = helper(nums)

        # LIS from right == LDS from left
        right = helper(nums[::-1])[::-1]

        res = n

        for i in range(n):
            # peak cannot be first or last element
            if left[i] > 1 and right[i] > 1:
                mountain_len = left[i] + right[i] - 1
                res = min(res, n - mountain_len)

        return res


print(Solution().minimumMountainRemovals([1,3,1])) # 0
print(Solution().minimumMountainRemovals([2,1,1,5,6,2,3,1])) # 3