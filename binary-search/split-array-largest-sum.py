# https://leetcode.com/problems/split-array-largest-sum/


# TC: O(n * log(sum(nums)))
# SC: O(1)
class Solution:
    def splitArray(self, nums, k: int) -> int:

        def partitions_needed(max_sum):

            partitions = 1
            curr_sum = 0

            for num in nums:

                if curr_sum + num <= max_sum:
                    curr_sum += num
                else:
                    curr_sum = num
                    partitions += 1

            return partitions

        low = max(nums)
        high = sum(nums)

        while low < high:

            mid = (low + high) // 2

            partitions = partitions_needed(mid)

            if partitions > k:
                low = mid + 1
            else:
                high = mid

        return low


print(Solution().splitArray([1, 4, 4], 3))       # 4
print(Solution().splitArray([1, 2, 3, 4, 5], 2)) # 9
print(Solution().splitArray([7, 2, 5, 10, 8], 2))# 18


# VARIATION:  What if we have negative number as well, so in that case our hi will be, hi = max(sum(nums), max(nums))
# here, low will be same as max(nums)
# this will Safety check for negative-heavy arrays rest is same as above