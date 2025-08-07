# https://leetcode.com/problems/subarray-sum-equals-k

# Number of subarrays that sum to equals to k.

# TC: O(N)
# SC: O(N)

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


# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/

# Longest Subarray With Sum K
def maxSubArrayLen(nums, k):

    max_len = 0
    seen = {0: -1}  # prefix_sum 0 at index -1 for edge case
    prefix_sum = 0

    for i, num in enumerate(nums):
        prefix_sum += num

        if prefix_sum - k in seen:
            max_len = max(max_len, i - seen[prefix_sum - k])

        # Only store first occurrence of a prefix_sum
        if prefix_sum not in seen:
            seen[prefix_sum] = i

    return max_len

print(maxSubArrayLen([1, -1, 5, -2, 3], 3))  # Output: 4
print(maxSubArrayLen([-2, -1, 2, 1], 1))  # Output: 2
print(maxSubArrayLen([1, 2, 3], 3))  # Output: 2
print(maxSubArrayLen([1, 2, 3], 6))  # Output: 3


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

        res = 0
        cur = 0
        freq = {0: 1}

        for i in nums:

            cur += i

            res += freq.get(cur - k, 0)

            freq[cur] = freq.get(cur, 0) + 1

        return res
    
print(Solution().numSubarraysWithSum([1, 1, 1], 2))  # Output: 2
