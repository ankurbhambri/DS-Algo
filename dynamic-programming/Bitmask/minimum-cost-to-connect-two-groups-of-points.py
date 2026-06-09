# https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points

import functools


class Solution:
    def connectTwoGroups(self, cost: list[list[int]]) -> int:

        m = len(cost)
        n = len(cost[0])

        # Precompute: Group 2 ke har point ke liye Group 1 se milne wali min cost
        min_costs_g2 = [min(col) for col in zip(*cost)]

        @functools.lru_cache(None)
        def dfs(i: int, mask: int) -> int:

            # Base Case: Jab Group 1 ke saare points connect ho chuke hain
            if i == m:

                ans = 0

                # Group 2 ke jo points bach gaye hain, unhe unke min cost wale option se connect karo
                for j in range(n):
                    if not (mask & (1 << j)):  # Agar j-th point connected nahi hai
                        ans += min_costs_g2[j]

                return ans

            res = float('inf')
            # Group 1 ke i-th point ko Group 2 ke har j-th point se connect karke check karo
            for j in range(n):
                res = min(res, cost[i][j] + dfs(i + 1, mask | (1 << j)))

            return res

        # 0th point of Group 1 se start karenge aur initial mask 0 hoga
        return dfs(0, 0)


print(Solution().connectTwoGroups([[15, 96], [36, 2]]))  # Output: 17
print(Solution().connectTwoGroups([[1, 3, 5], [4, 1, 1], [1, 5, 3]]))  # Output: 4