# https://leetcode.com/problems/majority-element/

# TC: O(n)
# SC: O(1)

class Solution:
    def majorityElement(self, nums):
        candidate = nums[0]
        c = 0
        for i in nums:
            if i == candidate:
                c += 1
            else:
                c -= 1
                if c == 0:
                    candidate = i
                    c += 1
        return candidate


print(Solution().majorityElement([3, 2, 3]))  # Output: 3
print(Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))  # Output: 2
print(Solution().majorityElement([1]))  # Output: 1
print(Solution().majorityElement([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]))  # Output: 10
