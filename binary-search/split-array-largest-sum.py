# https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums, k: int) -> int:

        def helper(m):

            partitions = 1
            curr_sum = 0

            for n in nums:

                if curr_sum + n <= m:
                    curr_sum += n

                else:
                    curr_sum = n
                    partitions += 1

            return partitions

        l = max(nums)
        r = max(sum(nums), max(nums)) # Safety check for negative-heavy arrays

        while l < r:
            m = (l + r) // 2

            partitions = helper(m)

            if partitions > k:
                l = m + 1 # too many partitions
            else:
                r = m # try smaller max_sum
        return l

print(Solution().splitArray([1,4,4], 3)) # 4
print(Solution().splitArray([1,2,3,4,5], 2)) # 9
print(Solution().splitArray([7,2,5,10,8], 2)) # 18