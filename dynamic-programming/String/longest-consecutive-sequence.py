# https://leetcode.com/problems/longest-consecutive-sequence/

# Using hash set to find the longest consecutive sequence in an array.

class Solution:
    def longestConsecutive(self, arr):

        arr = set(arr)
        res = 0
        for i in arr:
            if i - 1 not in arr:
                length = 0
                while i + length in arr:
                    length += 1
                res = max(length, res)

        return res


print(Solution().longestConsecutive([100, 4, 0, 200, 2, 3, 1]))  # Output: 4
print(Solution().longestConsecutive([0, 1, 2, 3, 4, 5]))  # Output: 6
print(Solution().longestConsecutive([1, 2, 3, 4, 5]))  # Output: 5
print(Solution().longestConsecutive([10, 20, 30, 40]))  # Output: 1
