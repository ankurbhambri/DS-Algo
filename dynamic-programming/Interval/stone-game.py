# https://leetcode.com/problems/stone-game/


# similar - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def stoneGame(self, piles: list[int]) -> bool:

        n = len(piles)

        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = piles[i]

        for length in range(2, n + 1):

            for i in range(n - length + 1):

                j = i + length - 1

                dp[i][j] = max(
                    piles[i] - dp[i + 1][j],
                    piles[j] - dp[i][j - 1]
                )

        return dp[0][n - 1] > 0


print(Solution().stoneGame([5, 3, 4, 5]))
print(Solution().stoneGame([3, 7, 2, 3]))