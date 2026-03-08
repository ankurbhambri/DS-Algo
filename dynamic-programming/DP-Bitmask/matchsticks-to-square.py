# https://leetcode.com/problems/matchsticks-to-square/description/


# Tumhe matchsticks ko use karke square banana hai. Square ki 4 sides hoti hain aur sabka length equal hona chahiye.

# backtracking

# TC: O(4^n) where n is the number of matchsticks
# SC: O(n) for the recursion stack
class Solution:
    def makesquare(self, matchsticks):

        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        side = total // 4

        matchsticks.sort(reverse=True)

        sides = [0,0,0,0]

        def dfs(i):

            if i == len(matchsticks):
                return True

            for j in range(4):

                if sides[j] + matchsticks[i] <= side:

                    sides[j] += matchsticks[i]

                    if dfs(i + 1):
                        return True

                    sides[j] -= matchsticks[i]

            return False

        return dfs(0)


# Bitmask DP

# TC: O(n * 2^n) where n is the number of matchsticks
# SC: O(2^n) for the dp array
class Solution:
    def makesquare(self, matchsticks):

        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        side = total // 4
        n = len(matchsticks)

        dp = [-1] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):

            if dp[mask] == -1:
                continue

            for i in range(n):

                if mask & (1 << i) == 0:

                    new_len = dp[mask] + matchsticks[i]

                    if new_len <= side:

                        new_mask = mask | (1 << i)

                        dp[new_mask] = new_len % side

        return dp[-1] == 0