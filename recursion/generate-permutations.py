# https://leetcode.com/problems/permutations/description/

from collections import deque
class Solution:
    def permute(self, nums):

        q = deque()
        q.append(((nums, [])))

        res = []
        while q:
            nums, path = q.popleft()
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                newNums = nums[:i] + nums[i+1:]
                q.append((newNums, path + [nums[i]]))
        return res

print(Solution().permute([1, 2, 3]))  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]] 
print(Solution().permute([0, 1]))  # [[0, 1], [1, 0]]
print(Solution().permute([1]))  # [[1]]
print(Solution().permute([]))  # [[]]
print(Solution().permute([1, 2, 3, 4]))  # All permutations of [1, 2, 3, 4]
print(Solution().permute([5, 6, 7]))  # All permutations of [5, 6, 7]
