# https://leetcode.com/problems/delete-and-earn/

from collections import Counter
from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        c = Counter(nums)
        nums = sorted(c.keys())

        e1, e2 = 0, 0

        for i, n in enumerate(nums):

            curr = n * c[n]

            # adjacent value can't take 4 == 3 + 1
            if i > 0 and n == nums[i - 1] + 1:
                e1, e2 = e2, max(curr + e1, e2)

            # now we can take the adjacent becasue not equal
            else:
                e1, e2 = e2, curr + e2

        return max(e1, e2)

print(Solution().deleteAndEarn([3,4,2]))  # Output: 6
print(Solution().deleteAndEarn([2,2,3,3,3,4]))  # Output: 9
print(Solution().deleteAndEarn([1,1,1,2,4,5,5,5,6]))  # Output: 18
print(Solution().deleteAndEarn([8,10,4,9,1,3,5,9,4,10]))  # Output: 37
