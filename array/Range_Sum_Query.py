# https://leetcode.com/problems/range-sum-query-immutable/


# O(N) computation, O(1) query, O(1) Space
class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums

        for i in range(1, len(nums)):
            self.nums[i] = self.nums[i] + self.nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:
        lf = self.nums[left - 1] if left != 0 else 0
        rf = self.nums[right]
        return rf - lf
