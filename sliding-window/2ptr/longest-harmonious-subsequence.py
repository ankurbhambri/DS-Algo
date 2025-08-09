# https://leetcode.com/problems/longest-harmonious-subsequence

# Question: Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
# A harmonious subsequence is a subsequence where the difference between its maximum and minimum element is exactly 1.


from collections import Counter

class Solution:
    def findLHS(self, nums):

        res = 0
        count = Counter(nums)  # Count frequencies
        
        for num in count:
            if num + 1 in count:
                res = max(res, count[num] + count[num + 1]) # Subsequence, order should be same but can delete/skip elements in between
        return res


print(Solution().findLHS([1,3,2,2,5,4]))  # Output: 5
print(Solution().findLHS([1,2,3,4]))  # Output: 2
print(Solution().findLHS([1,1,1,1]))  # Output: 0
print(Solution().findLHS([1,2,3,2,3,4,5,6]))  # Output: 6
