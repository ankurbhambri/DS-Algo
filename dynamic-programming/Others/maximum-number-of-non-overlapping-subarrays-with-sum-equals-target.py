# https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/

class Solution:
    def maxNonOverlapping(self, nums: list[int], target: int) -> int:

        seen = {0}
        curr = 0
        ans = 0

        for x in nums:

            curr += x

            if curr - target in seen:

                ans += 1

                curr = 0
                seen = {0}

            else:
                seen.add(curr)

        return ans


print(Solution().maxNonOverlapping([0,0,0], 0)) # 3
print(Solution().maxNonOverlapping([1,1,1,1,1], 2)) # 2
print(Solution().maxNonOverlapping([-1,3,5,1,4,2,-9], 6)) # 2
print(Solution().maxNonOverlapping([-2,6,6,3,5,4,1,2,8], 10)) # 3