# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/


# TC: O(n log n)
# SC: O(1)
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:

        def helper(cap):

            d = 1
            curr = 0

            for w in weights:

                if curr + w <= cap:
                    curr += w

                else:
                    d += 1
                    curr = w

            return d <= days

        l = max(weights)
        r = sum(weights)

        while l < r:

            m = (l + r) // 2

            if helper(m):
                r = m

            else:
                l = m + 1

        return l


print(Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)) # 15
print(Solution().shipWithinDays([3, 2, 2, 4, 1, 4], 3)) # 6