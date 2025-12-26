class Solution:
    def minimumSumSubarray(self, nums, l, r):

        n = len(nums)
        
        # Build prefix sum
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        min_sum = float('inf')
        
        # Try all subarray lengths from l to r
        for length in range(l, r + 1):
            for i in range(n - length + 1):
                curr_sum = prefix[i + length] - prefix[i]
                if curr_sum > 0:
                    min_sum = min(min_sum, curr_sum)
        
        return min_sum if min_sum != float('inf') else -1


print(Solution().minimumSumSubarray([3, -2, 1, 4], 2, 3))  # Output: 1
print(Solution().minimumSumSubarray([-1, -2, -3], 1, 2))      # Output: -1
