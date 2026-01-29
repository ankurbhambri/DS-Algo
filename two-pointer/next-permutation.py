# https://leetcode.com/problems/next-permutation/description/

# Narayana Pandita Technique

class Solution:
    def nextPermutation(self, nums):

        n = len(nums)
        k = -1

        # Step 1: Pehla decreasing element dhundein
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                k = i
                break

        # Step 2: Agar k nahi mila, matlab array fully descending hai (e.g., [3,2,1])
        if k == -1:
            nums.reverse() # In-place reverse
            return

        # Step 3: k ke right mein nums[k] se just bada number dhundein
        l = -1
        for i in range(n - 1, k, -1):
            if nums[i] > nums[k]:
                l = i
                break

        # Step 4: Swap karein
        nums[k], nums[l] = nums[l], nums[k]

        # Step 5: k ke aage wale hisse ko in-place reverse karein
        # Slicing use karke wapas assign karne ke liye [:] use karein
        nums[k + 1:] = reversed(nums[k + 1:])


print(Solution().nextPermutation([1, 2, 3]))  # Output: [1, 3, 2]
print(Solution().nextPermutation([3, 2, 1]))  # Output: [1, 2, 3]
print(Solution().nextPermutation([1, 1, 5]))  # Output: [1, 5, 1]
print(Solution().nextPermutation([1, 3, 2]))  # Output: [2, 1, 3]