# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/description/


# TC: O(n * 2^n)
# SC: O(2^n) for dp array
class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:

        total = sum(nums)

        if total % k:
            return False

        target = total // k
        n = len(nums)

        dp = [-1] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):

            if dp[mask] == -1:
                continue

            for i in range(n):

                if mask & (1 << i):
                    continue

                if dp[mask] + nums[i] > target:
                    continue

                next_mask = mask | (1 << i)

                dp[next_mask] = (dp[mask] + nums[i]) % target

        return dp[(1 << n) - 1] == 0


print(Solution().canPartitionKSubsets([1, 2, 3, 4], 3))  # Output: False
print(Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4))  # Output: True