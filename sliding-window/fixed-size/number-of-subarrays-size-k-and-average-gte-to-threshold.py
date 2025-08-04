# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

class Solution:
    def numOfSubarrays(self, arr, k: int, threshold: int) -> int:

        cur_sum = sum(arr[:k])

        res = 1 if cur_sum // k >= threshold else 0

        for i in range(k, len(arr)):

            cur_sum += arr[i] - arr[i - k]

            if cur_sum // k >= threshold:

                res += 1

        return res


print(Solution().numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4))  # 3
print(Solution().numOfSubarrays([1,2,3,4,5], 2, 3))  # 2
print(Solution().numOfSubarrays([1,2,3,4,5], 3, 4))  # 1
print(Solution().numOfSubarrays([1,2,3,4,5], 4, 5))  # 0
