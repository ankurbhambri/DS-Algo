# similar - https://leetcode.com/problems/binary-subarrays-with-sum/


def subarraySum(nums, k):

    sum_val = 0
    res = 0
    prefixSum = {0: 1}

    for i in nums:

        sum_val += i

        res += prefixSum.get(sum_val - k, 0)

        prefixSum[sum_val] = 1 + prefixSum.get(sum_val, 0)

    return res

# Example usage
nums = [1, 1, 1]
k = 2
print(subarraySum(nums, k))  # Output: 2
# Explanation: There are two subarrays that sum to 2: [1, 1] and [1, 1]
nums = [1, 2, 3]
k = 3
print(subarraySum(nums, k))  # Output: 2
# Explanation: There are two subarrays that sum to 3: [1, 2] and [3]
nums = [1, 2, 1, 2, 1]
k = 3
print(subarraySum(nums, k))  # Output: 4
# Explanation: There are four subarrays that sum to 3: [1, 2], [2, 1], [1, 2], and [1, 2]