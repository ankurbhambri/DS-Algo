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
