# https://leetcode.com/problems/continuous-subarray-sum/


class Solution:
    def checkSubarraySum(self, nums, k):

        prefix_mod = 0
        seen = {0: -1}

        for i in range(len(nums)):

            prefix_mod = (prefix_mod + nums[i]) % k

            if prefix_mod in seen:
                # ensures that the size of subarray is at least 2
                if i - seen[prefix_mod] > 1:
                    return True
            else:
                # mark the value of prefix_mod with the current index.
                seen[prefix_mod] = i

        return False


print(Solution().checkSubarraySum([0, 0], 0))  # True
print(Solution().checkSubarraySum([23, 2, 4, 6, 7], 6))  # True
print(Solution().checkSubarraySum([23, 2, 6, 4, 7], 6))  # True
print(Solution().checkSubarraySum([23, 2, 6, 4, 7], 13))  # False