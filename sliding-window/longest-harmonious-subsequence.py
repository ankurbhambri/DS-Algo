# https://leetcode.com/problems/longest-harmonious-subsequence

from collections import Counter

class Solution:
    def findLHS(self, nums):
        count = Counter(nums)  # Count frequencies
        res = 0
        
        for num in count:
            if num + 1 in count:
                res = max(res, count[num] + count[num + 1])
        
        return res


print(Solution().findLHS([1,3,2,2,5,4]))  # Output: 5
print(Solution().findLHS([1,2,3,4]))  # Output: 2
print(Solution().findLHS([1,1,1,1]))  # Output: 0
print(Solution().findLHS([1,2,3,2,3,4,5,6]))  # Output: 6
