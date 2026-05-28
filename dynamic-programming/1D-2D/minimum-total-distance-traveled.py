# https://leetcode.com/problems/minimum-total-distance-traveled


class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:

        robot.sort()
        factory.sort()

        # Flatten factories: if factory j has capacity c, treat it as c individual slots
        # This simplifies the DP but can be optimized for space.
        factory_slots = []
        for pos, cap in factory:
            factory_slots.extend([pos] * cap)

        n, m = len(robot), len(factory_slots)

        # dp[i][j] = min distance for first i robots using first j factory slots
        # Initialize with a very large value
        dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for j in range(1, m + 1):
            dp[0][j] = 0 # 0 robots always cost 0
            for i in range(1, n + 1):

                # Option 1: Don't use the j-th factory slot
                dp[i][j] = dp[i][j-1]

                # Option 2: Use the j-th factory slot for the i-th robot
                dist = abs(robot[i-1] - factory_slots[j-1])
                if dp[i-1][j-1] != float('inf'):
                    dp[i][j] = min(dp[i][j], dp[i-1][j-1] + dist)

        return dp[n][m]


print(Solution().minimumTotalDistance([1, -1], [[-2, 1], [2, 1]])) # Output: 2
print(Solution().minimumTotalDistance([0, 4, 6], [[2, 2], [6, 2]])) # Output: 4