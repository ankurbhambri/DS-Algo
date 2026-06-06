# https://leetcode.com/problems/largest-divisible-subset/


# similar - https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii

# TC: O(n^2)
# SC: O(n)
class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:

        nums.sort()
        n = len(nums)

        dp = [1] * n
        parent = [-1] * n

        max_len = 1
        last_idx = 0

        for i in range(n):
            for j in range(i):

                if nums[i] % nums[j] == 0:

                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        parent[i] = j

            if dp[i] > max_len:
                max_len = dp[i]
                last_idx = i

        ans = []

        while last_idx != -1:
            ans.append(nums[last_idx])
            last_idx = parent[last_idx]

        return ans[::-1]


print(Solution().largestDivisibleSubset([1, 2, 3])) # [1, 2] or [1, 3]
print(Solution().largestDivisibleSubset([1, 2, 4, 8])) # [1, 2, 4, 8]