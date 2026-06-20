# https://leetcode.com/problems/maximum-building-height


# TC: O(n log n) due to sorting
# SC: O(n) due to sorting
class Solution:
    def maxBuilding(self, n: int, restrictions: list[list[int]]) -> int:

        restrictions = [[1, 0]] + restrictions + [[n, n - 1]]

        restrictions.sort()

        m = len(restrictions)

        # Yha pe hum left to right pass karenge, jisme hum ensure karenge ki increasing sequence ko zyada height mile.
        for i in range(1, m):
            dist = restrictions[i][0] - restrictions[i - 1][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i - 1][1] + dist)

        # Yha pe hum right to left pass karenge, jisme hum ensure karenge ki decreasing sequence ko zyada height mile.
        for i in range(m - 2, -1, -1):
            dist = restrictions[i + 1][0] - restrictions[i][0]
            restrictions[i][1] = min(restrictions[i][1], restrictions[i + 1][1] + dist)

        res = 0
        for i in range(1, m):

            l = restrictions[i - 1][1]

            r = restrictions[i][1]

            dist = restrictions[i][0] - restrictions[i - 1][0]

            peak = (l + r + dist) // 2

            res = max(res, peak)

        return res


print(Solution().maxBuilding(5, [[2, 1], [4, 1]])) # Output: 2
print(Solution().maxBuilding(6, [[1, 0], [3, 2]])) # Output: 2