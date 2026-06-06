# https://leetcode.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum/


# TC: O(n)
# SC: O(n)
class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:

        n = len(arr)

        best = [float('inf')] * n

        pref = {0: -1}
        curr = 0

        ans = float('inf')
        best_so_far = float('inf')

        for i, x in enumerate(arr):

            curr += x

            if curr - target in pref:

                j = pref[curr - target]

                curr_len = i - j

                if j >= 0:
                    ans = min(ans, curr_len + best[j])

                best_so_far = min(best_so_far, curr_len)

            best[i] = best_so_far

            pref[curr] = i

        return ans if ans != float('inf') else -1


print(Solution().minSumOfLengths([7, 3, 4, 7], 7))
print(Solution().minSumOfLengths([3, 2, 2, 4, 3], 3))