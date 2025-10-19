# https://leetcode.com/problems/range-sum-query-immutable/
# https://www.hackerrank.com/challenges/crush/problem
# https://cses.fi/problemset/task/1646


# O(N) computation, O(1) query, O(1) Space
class NumArray:
    def __init__(self, nums):

        self.nums = nums
        # precompute prefix sums
        for i in range(1, len(nums)):
            self.nums[i] += self.nums[i - 1]

    def sumRange(self, left: int, right: int) -> int:

        lf = self.nums[left - 1] if left != 0 else 0
        rf = self.nums[right]

        return rf - lf


# Test case 1
nums = [1, 2, 3, 4, 5]
num_array = NumArray(nums)

print(num_array.sumRange(1, 3))  # 9

print(num_array.sumRange(0, 4))  # 15

print(num_array.sumRange(0, 1))  # 3

print(num_array.sumRange(2, 2))  # 3

# Test case 2
nums = [-2, 0, 3, -5, 2, -1]
num_array = NumArray(nums)
print(num_array.sumRange(0, 2))  # 1


# Variation

# Given an array of 1's and 0's, find number of 1's in a given range [L, R].
class NumOnes:
    def __init__(self, nums):

        self.nums = nums
        # precompute prefix sums
        for i in range(1, len(nums)):
            self.nums[i] += self.nums[i - 1]

    def countOnes(self, left: int, right: int) -> int:

        lf = self.nums[left - 1] if left != 0 else 0
        rf = self.nums[right]

        return rf - lf

print("Variation Test Cases")
nums = [1, 0, 1, 1, 0, 1, 0, 0, 1]
num_ones = NumOnes(nums)
print(num_ones.countOnes(0, 8))  # 5
print(num_ones.countOnes(1, 3))  # 2
print(num_ones.countOnes(4, 7))  # 1
print(num_ones.countOnes(2, 5))  # 3
