# https://leetcode.com/problems/subarray-sums-divisible-by-k/


# TC: O(N)
# SC: O(N)
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:

        sum_val = 0
        res = 0
        prefixSum = {0: 1}

        for i in nums:

            sum_val += i

            sum_val = sum_val % k

            res += prefixSum.get(sum_val, 0)

            prefixSum[sum_val] = 1 + prefixSum.get(sum_val, 0)

        return res


print(Solution().subarraysDivByK([5], 9)) # Output: 0
print(Solution().subarraysDivByK([4, 5, 0, -2, -3, 1], 5)) # Output: 7