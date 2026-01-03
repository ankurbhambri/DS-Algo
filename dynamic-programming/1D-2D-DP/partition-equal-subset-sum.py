# https://leetcode.com/problems/partition-equal-subset-sum/description/

class Solution:
    def canPartition(self, nums):

        total = sum(nums)
        if total % 2 != 0:
            return False  # Can't split an odd total into two equal parts
        
        target = total // 2
        n = len(nums)
        
        # dp[i] means whether a subset sum i can be formed
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: 0 sum is always possible (empty set)

        for num in nums:
            for i in range(target, num - 1, -1):  # Traverse backwards to avoid reuse
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]

print(Solution().canPartition([1, 5, 11, 5]))  # Output: True
print(Solution().canPartition([1, 2, 3, 5]))   # Output: False