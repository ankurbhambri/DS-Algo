# https://leetcode.com/problems/subarrays-with-k-different-integers/

# This problem is a variation of the sliding window problem where we need to count the number of subarrays that contain exactly K distinct integers.

'''
Sometimes the problem says “EXACTLY K distinct” (e.g., “Count subarrays with exactly K distinct numbers”).

We do this: exactlyK = atMostK(K) - atMostK(K-1)

Because: All subarrays with at most K distinct - All subarrays with at most (K-1) distinct = Subarrays with exactly K distinct.
'''


class Solution:
    def subarraysWithKDistinct(self, nums, K: int) -> int:
        def atMost(k):
            l = 0
            res = 0
            count = {}
            for r in range(len(nums)):
                count[nums[r]] = count.get(nums[r], 0) + 1
                while len(count) > k:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        del count[nums[l]]
                    l += 1
                res += (r - l + 1)
            return res

        return atMost(K) - atMost(K-1)


print(Solution().subarraysWithKDistinct([1, 2, 1, 2, 3], 2))  # 7
print(Solution().subarraysWithKDistinct([1, 2, 1, 3, 4], 3))  # 3
print(Solution().subarraysWithKDistinct([1, 2, 1, 2, 3], 1))  # 5
print(Solution().subarraysWithKDistinct([1, 2, 1, 2, 3], 4))  # 0
