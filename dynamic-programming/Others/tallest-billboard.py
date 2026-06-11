# https://leetcode.com/problems/tallest-billboard/


# TC: O(N * S), where S is the sum of all rods and N is the number of rods
# SC: O(S)
class Solution:
    def tallestBillboard(self, rods: list[int]) -> int:

        dp = {0: 0} # {diff: max taller height}

        # for example dp[3] = 8, means 8 is the tallest rod height and 3 means difference in between smaller and taller

        # d = Taller rod (t) - shorter rod (s)

        for r in rods:

            new_dp = dp.copy()

            for d, t in dp.items():

                # Choice 1: Taller par lagao

                # (t + r) - s -> t - s + r, here we can substitue d = t - s will get, d + r, and we are adding t + r new value

                new_dp[d + r] = max(new_dp.get(d + r, 0), t + r)

                # Choice 2: skip
                new_dp[d] = max(new_dp[d], t)

                # Choice 3:

                # 3.1 Case A: Shorter par lagao, but shorter still chota h, still t is taller

                # t - (s + r) -> t - s - r -> d - r

                new_dp[d - r] = max(new_dp.get(d - r, 0), t)

                # 3.2 Case B: Shorter become Taller

                # here we are doing s + r, but we don't have s + r, so

                # we have d = t - s, this can write it as s = t - d,

                # this we can substitute with s -> t - d + d

                new_dp[r - d] = max(new_dp.get(r - d, 0), t + r - d)

            dp = new_dp

        return dp.get(0, 0)


print(Solution().tallestBillboard([1, 2, 3, 6]))  # Output: 6
print(Solution().tallestBillboard([1, 2, 3, 4, 5, 6]))  # Output: 10