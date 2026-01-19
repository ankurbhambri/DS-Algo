# https://leetcode.com/problems/single-number/

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. Solve in linear complexity


class Solution:
    def singleNumber(self, nums):
        a = 0
        for n in nums:
            a ^= n
        return a


print(Solution().singleNumber([4, 1, 2, 1, 2]))
print(Solution().singleNumber([2, 2, 1]))
print(Solution().singleNumber([1]))
print(Solution().singleNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
print(Solution().singleNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]))


# https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums):

        xor_all = 0

        # Step 1: XOR of all numbers
        for n in nums:
            xor_all ^= n

        # Step 2: rightmost set bit
        mask = xor_all & -xor_all

        a = 0
        b = 0

        # Step 3: divide into two groups
        for n in nums:
            if n & mask:
                a ^= n
            else:
                b ^= n

        return [a, b] 

print(Solution().singleNumber([0, 1]))  # [0,1]
print(Solution().singleNumber([-1, 0]))  # [-1,0]
print(Solution().singleNumber([2, 1, 2, 3, 4, 1]))  # [3,4]
print(Solution().singleNumber([1, 2, 1, 3, 2, 5]))  # [3,5]