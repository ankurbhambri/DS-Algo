# https://leetcode.com/problems/subarray-sum-equals-k


def subarraySum(nums, k):

    sum_val = 0
    res = 0
    prefixSum = {0: 1}

    for i in nums:

        sum_val += i

        res += prefixSum.get(sum_val - k, 0)

        prefixSum[sum_val] = 1 + prefixSum.get(sum_val, 0)

    return res


print(subarraySum([1, 1, 1], 2))  # Output: 2 -> [1, 1] and [1, 1]
print(subarraySum([1, 2, 3], 3))  # Output: 2 -> [1, 2] and [3]
print(subarraySum([1, 2, 1, 2, 1], 3))  # Output: 4 -> [1, 2], [2, 1], [1, 2], [1, 2]


# Variant: Return True if there exists a subarray with sum equal to k, otherwise return False.
def hasSubarraySum(nums, k):
    sum_val = 0
    prefixSum = {0: 1}

    for i in nums:
        sum_val += i

        if (sum_val - k) in prefixSum:
            return True

        prefixSum[sum_val] = 1 + prefixSum.get(sum_val, 0)

    return False


print(hasSubarraySum([5], 5)) # True
print(hasSubarraySum([1, 1, 1], 2)) # True
print(hasSubarraySum([-1, -2, -3, -4], -15)) # False
print(hasSubarraySum([3, 4, 7, 2, -3, 1, 4, 2, 1, -14], -10)) # False


# Without extra space (Just check True or False)
def subarraySumExistsPositiveNums(nums, k):

    l = 0
    window_sum = 0

    for r in range(len(nums)):
        window_sum += nums[r]

        while window_sum > k:
            window_sum -= nums[l]
            l += 1
        
        if window_sum == k:
            return True

    return False


print(subarraySumExistsPositiveNums([1, 1, 1], 2)) # True
print(subarraySumExistsPositiveNums([1, 2, 3], 3)) # True
print(subarraySumExistsPositiveNums([1, 3, 5, 23, 2], 7)) # False
print(subarraySumExistsPositiveNums([100, 101, 102, 103], 2)) # False


# similar: https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums, k: int) -> int:
        freq = {0: 1}
        res = 0
        cur = 0
        for i in nums:
            cur += i
            res += freq.get(cur - k, 0)
            freq[cur] = freq.get(cur, 0) + 1
        return res
    
print(Solution().numSubarraysWithSum([1, 1, 1], 2))  # Output: 2
