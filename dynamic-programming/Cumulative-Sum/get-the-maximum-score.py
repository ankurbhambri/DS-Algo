# https://leetcode.com/problems/get-the-maximum-score/

class Solution:
    def maxSum(self, nums1: list[int], nums2: list[int]) -> int:

        MOD = 10**9 + 7

        i = j = 0
        s1 = s2 = 0

        while i < len(nums1) and j < len(nums2):

            if nums1[i] < nums2[j]:
                s1 += nums1[i]
                i += 1

            elif nums1[i] > nums2[j]:
                s2 += nums2[j]
                j += 1

            else:

                best = max(s1, s2) + nums1[i] # when values are mmatching, get the max score from both sides

                s1 = best
                s2 = best

                i += 1
                j += 1

        while i < len(nums1):
            s1 += nums1[i]
            i += 1

        while j < len(nums2):
            s2 += nums2[j]
            j += 1

        return max(s1, s2) % MOD


print(Solution().maxSum([2, 4, 5, 8, 10], [4, 6, 8, 9]))
print(Solution().maxSum([1, 3, 5, 7, 9], [3, 5, 100]))