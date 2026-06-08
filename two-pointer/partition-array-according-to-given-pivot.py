# https://leetcode.com/problems/partition-array-according-to-given-pivot


# TC: O(n)
# SC: O(n)
class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:

        n = len(nums)

        res = [0] * n

        l, r = 0, n - 1

        j = n - 1

        for i in range(n):

            if nums[i] < pivot:
                res[l] = nums[i]
                l += 1

            if nums[j] > pivot:
                res[r] = nums[j]
                r -= 1

            j -= 1

        while l <= r:
            res[l] = pivot
            l += 1

        return res


print(Solution().pivotArray([-3, 4, 3, 2], 2)) # [-3, 3, 4, 2]
print(Solution().pivotArray([9, 12, 5, 10, 14, 3, 10], 10)) # [9, 5, 3, 10, 10, 12, 14]