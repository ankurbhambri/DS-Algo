# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums):
        n = len(nums)
        l, r = 0, n - 1
        res = [0] * n
        pos = n - 1

        while l <= r:

            if abs(nums[l]) > abs(nums[r]):
                res[pos] = nums[l] ** 2
                l += 1

            else:
                res[pos] = nums[r] ** 2
                r -= 1

            pos -= 1

        return res


print(Solution().sortedSquares([-4, -1, 0, 3, 10]))  # [0, 1, 9, 16, 100]
print(Solution().sortedSquares([-7, -3, 2, 3, 11]))  # [4, 9, 9, 49, 121]
print(Solution().sortedSquares([-5, -3, -2, -1]))  # [1, 4, 9, 25]
print(Solution().sortedSquares([0, 1, 2, 3, 4]))  # [0, 1, 4, 9, 16]