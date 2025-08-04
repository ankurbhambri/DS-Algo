# https://leetcode.com/problems/patching-array/

class Solution:
    def minPatches(self, nums, n: int) -> int:

        i = 0
        res = 0
        patch = 0

        while patch < n:

            if i < len(nums) and patch + 1 >= nums[i]:

                patch += nums[i]

                i += 1

            else:

                patch += (patch + 1)

                res += 1

        return res


print(Solution().minPatches([1, 3], 6))  # Output: 1
print(Solution().minPatches([1, 5, 10], 20))  # Output: 2
print(Solution().minPatches([1, 2, 31, 33], 2147483647))  # Output: 28
print(Solution().minPatches([], 7))  # Output: 3
