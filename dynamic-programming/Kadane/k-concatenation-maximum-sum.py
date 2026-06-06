# https://leetcode.com/problems/k-concatenation-maximum-sum/

# TC: O(n)
# SC: O(1)
class Solution:
    def kConcatenationMaxSum(self, arr: list[int], k: int) -> int:

        MOD = 10**9 + 7

        def kadane(nums):

            curr = best = 0

            for x in nums:
                curr = max(0, curr + x)
                best = max(best, curr)

            return best

        if k == 1:
            return kadane(arr) % MOD

        total = sum(arr)

        best_two = kadane(arr * 2)

        if total <= 0: # if total is less than or equal to 0, we can't add more arrays to increase the sum, so we just return the best sum of two arrays
            return best_two % MOD

        # In case total is greater than 0
        prefix = suffix = 0

        curr = 0
        for x in arr:
            curr += x
            prefix = max(prefix, curr)

        curr = 0
        for x in reversed(arr):
            curr += x
            suffix = max(suffix, curr)

        # formula is confusing but it works, we can break the k arrays into 3 parts, suffix of first array, prefix of last array and total sum of middle arrays
        ans = suffix + prefix + (k - 2) * total

        return ans % MOD


print(Solution().kConcatenationMaxSum([1, 2], 3))  # Output: 9
print(Solution().kConcatenationMaxSum([1, -2, 1], 5))  # Output: 2