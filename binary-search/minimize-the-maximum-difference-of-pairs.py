# https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs

class Solution:

    def minimizeMax(self, nums, p):

        nums.sort()
        n = len(nums)
        
        # Find the number of valid pairs by greedy approach
        def countValidPairs(threshold):
            index, count = 0, 0
            while index < n - 1:
                # If a valid pair is found, skip both numbers.
                if nums[index + 1] - nums[index] <= threshold:
                    count += 1
                    index += 2 # jump to next adjacent pair except the next element.
                else:
                    index += 1
            return count
        
        left, right = 0, nums[-1] - nums[0] # max difference
        while left < right:
            mid = left + (right - left) // 2

            # If there are enough pairs, look for a smaller threshold.
            # Otherwise, look for a larger threshold.
            if countValidPairs(mid) >= p:
                right = mid
            else:
                left = mid + 1

        return left

print(Solution().minimizeMax([1, 3, 6, 19, 20], 2)) # Output: 2
print(Solution().minimizeMax([1, 2, 3, 4, 5], 2)) # Output: 1
print(Solution().minimizeMax([1, 10, 100, 1000], 1)) # Output: 999
print(Solution().minimizeMax([1, 2, 3, 4, 5, 6], 3)) # Output: 1
print(Solution().minimizeMax([1, 2, 3, 4, 5, 6], 4)) # Output: 1
print(Solution().minimizeMax([1, 3, 6, 19, 20, 21], 3)) # Output: 2
