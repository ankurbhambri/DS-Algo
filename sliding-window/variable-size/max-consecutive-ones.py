# https://leetcode.com/problems/max-consecutive-ones-iii/

'''
    If the number of zeros in the window (zeros) exceeds k, the window is invalid (we can't flip more than k zeros).
    Shrink the window from the left (l) until zeros <= k:

    If nums[l] == 0, decrement zeros (since we're removing a zero from the window).
    Increment l to shrink the window.


    This ensures the window always has at most k zeros.
'''

class Solution:
    def longestOnes(self, nums, k: int) -> int:
        l = 0
        zeros = 0
        max_len = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeros += 1

            while zeros > k:
                if nums[l] == 0:
                    zeros -= 1
                l += 1

            max_len = max(max_len, r - l + 1)

        return max_len


print(Solution().longestOnes([1,1,0,0,1,1,0,1], 2))  # Output: 6
print(Solution().longestOnes([0,0,1,1,0,0,1,1], 1))  # Output: 4
print(Solution().longestOnes([1,0,1,0,1,0], 3))  # Output: 6
print(Solution().longestOnes([1,1,1,1,1], 0))  # Output: 5
