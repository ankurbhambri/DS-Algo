# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/


class Solution:
    def maximumSubarraySum(self, nums, k: int) -> int:

        l = 0
        sm = 0
        res = 0
        seen = set()

        for r in range(len(nums)):

            sm += nums[r]

            while nums[r] in seen or r - l + 1 > k:
                seen.remove(nums[l])
                sm -= nums[l]
                l += 1
            
            seen.add(nums[r])

            if r - l + 1 == k:
                res = max(res, sm)
            
        return res



print(Solution().maximumSubarraySum([1,5,4,2,9,9,9], 3))  # 15
print(Solution().maximumSubarraySum([1,2,3,4,5], 2))  # 9
print(Solution().maximumSubarraySum([1,2,1,2,1,2], 2))  # 3
print(Solution().maximumSubarraySum([1,2,3,4,5], 3))  # 12


# Variation of distinct-sum problem (LC 2461) but only returns True/False.

def has_unique_window(nums, k):
    seen = set()
    l = 0
    for r in range(len(nums)):
        while nums[r] in seen:
            seen.remove(nums[l])
            l += 1
        seen.add(nums[r])
        if r - l + 1 == k:
            return True
    return False

print(has_unique_window([1,2,3,4,1,2], 4))  # True ([1,2,3,4])
print(has_unique_window([1,1,1,1], 2))     # False
