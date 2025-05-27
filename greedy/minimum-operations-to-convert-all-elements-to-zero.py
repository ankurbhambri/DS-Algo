# https://leetcode.com/problems/minimum-operations-to-convert-all-elements-to-zero/

class Solution:
    def minOperations(self, nums):
        s = [0]
        res = 0
        for a in nums:
            while s and s[-1] > a:
                s.pop()
            if not s or s[-1] < a:
                res += 1
                s.append(a)
        return res

print(Solution().minOperations([3, 1, 2, 1]))  # Output: 3
print(Solution().minOperations([1, 2, 1, 2, 1, 2]))  # Output: 4
